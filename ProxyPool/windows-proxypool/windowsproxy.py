import io, sys, time, re, os
import winreg

# 表项路径
xpath = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"


# 设定代理,enable:是否开启,proxyIp:代理服务器ip及端口,IgnoreIp:忽略代理的ip或网址
def setProxy(enable, proxyIp, IgnoreIp):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, xpath, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, enable)
        winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, proxyIp)
        winreg.SetValueEx(key, "ProxyOverride", 0, winreg.REG_SZ, IgnoreIp)
    except Exception as e:
        print("ERROR: " + str(e.args))
    finally:
        None


# 开启，定义代理服务器ip及端口，忽略ip内容(分号分割)
def enableProxy():
    proxyIP = "172.21.18.21:8080"
    IgnoreIp = "172.*;192.*;"
    print(" Setting proxy")
    setProxy(1, proxyIP, IgnoreIp)
    print(" Setting success")


# 关闭清空代理
def disableProxy():
    print(" Empty proxy")
    setProxy(0, "", "")
    print(" Empty success")


def main():
    place = input("where are you?(home or ls)\n")
    try:
        if place == "home":
            disableProxy()
        elif place == "ls":
            enableProxy()
        else:
            print("please input 'home' or 'ls'(longshine)!")
            main()
    except Exception as e:
        print("ERROR: " + str(e.args))
    finally:
        pass


if __name__ == '__main__':
    main()