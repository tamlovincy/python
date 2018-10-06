# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:33:09 2018

@author: Danling
"""

from tkinter import *
import tkinter.messagebox as messagebox
import time
import os


window = Tk()
window.title('倒计时') # 窗口标题
window.geometry('200x200') # 窗口大小

label = Label(window, text='请输入秒数') # 输入提示语
label.grid(row=1, column=0)
label.pack()

inp = Entry(window) # 输入秒数框
inp.pack()


def handle():
   if not inp.get().isdigit():
       messagebox.showinfo('警告', '输入内容不是数字！')
   else:
       counter_down = Label(window)
       counter_down.config(font=("Courier", 44))
       counter_down.pack(fill=BOTH)
       
       counter = int(inp.get()) # 输入的秒数
       
       while counter > 0:
           counter_down['text'] = str(counter)
           window.update()
           time.sleep(1)
           counter -= 1
           
       os._exit(0) # 倒计时结束，退出

       
btn = Button(window, text='开始倒计时', command=handle).pack()
window.mainloop()