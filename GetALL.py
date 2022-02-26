 #!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib.parse
import urllib.request
import re
import os


# html=html.decode('utf-8')#python3
header =\
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        "referer": "https://image.baidu.com"
        }

url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word={word}+&pn={pageNum}'
n = 0
j = 1
keyword = input("搜索内容：")
keywords=keyword
keyword = urllib.parse.quote(keyword, "utf-8")
# url1 = url.format(word= keyword,pageNum=str(n))
while(n<30000):
    error = 0
    n += 50
    url1 = url.format(word= keyword,pageNum=str(n))
    rep = urllib.request.Request(url1,headers=header)
    rep = urllib.request.urlopen(rep)
    try:
        #html = html.decode('utf-8')  # python3
        html = rep.read().decode("utf-8")
        print(html)


    except:
        print("XX:")
        error=1
        print("str(n)")
    if error == 1:
        continue
    p = re.compile("objURL.*?\.jpg")
    s = p.findall(html)
    # if not os.path.exists('D:/GIT/jandan_spider/images'):
    #     os.makedirs('D:/GIT/jandan_spider/images')
    with open("testpic.txt","a") as f:
        for i in s :
            i = i.replace('objURL":"','')
            i = i.replace('thumbURL":"', '')
            print(i)
            f.write(i)
            f.write("\n")
            try:
              urllib.request.urlretrieve(i, "D:/GIT/jandan_spider/PLMM/{SSNR}.{num}.jpg".format(SSNR=keywords, num=j))
            except:
                print("XXXXX:")
                error = 1
                print("str(n)")
                j += 1
            if error == 1:
                continue

            j+=1
        f.close()
print("toal:"+str(j))







