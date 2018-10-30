import tkinter as tk
import os
import sys
import requests
from proxypool.scheduler import Scheduler
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def startServer():
    try:
        s = Scheduler()
        s.run()
    except:
        startServer()

window = tk.Tk()
window.title('window-proxy-autoselection')
window.geometry('200x200')

var1 = tk.StringVar()
l = tk.Label(window, bg='white', width=20, height=3,textvariable=var1)
l.pack()

def setText():
    startServer()
    value = get_proxy()
    var1.set(value)

def get_proxy():
    r = requests.get('http://127.0.0.1:5555/random')
    return r.text

b1 = tk.Button(window, text='开启服务器', width=15,
              height=2, command=setText)
b1.pack()

b1 = tk.Button(window, text='随机生成', width=15,
              height=2, command=setText)
b1.pack()


b2 = tk.Button(window, text='开始代理', width=15,
              height=2, command=setText)
b2.pack()

b3 = tk.Button(window, text='取消代理', width=15,
              height=2, command=setText)
b3.pack()

# var2 = tk.StringVar()
# var2.set((11,22,33,44))
# lb = tk.Listbox(window, listvariable=var2)
# list_items = [1,2,3,4]
# for item in list_items:
#     lb.insert('end', item)
# lb.insert(1, 'first')
# lb.insert(2, 'second')
# lb.delete(2)
# lb.pack()





window.mainloop()