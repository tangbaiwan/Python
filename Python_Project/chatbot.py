import itchat
import requests
from retry import retry
def get_reply(keyword):
    try:
        url = f"https://open.drea.cc/bbsapi/chat/get?keyWord={keyword}&userName=type%3Dbbs"
        res = requests.get(url)
        data = res.json()
        return data['data']['reply']
    except:
        return "opps, 我还很笨，不造你在说啥"

@itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
def auto_reply(msg):
    reply = "execuse me?"
    try:
        reply = get_reply(msg.text)
    except:
        pass
    finally:
        print(f'[In] {msg.text} \t [Out] {reply}')
        return reply


