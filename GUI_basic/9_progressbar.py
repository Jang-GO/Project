import tkinter.ttk as ttk
from tkinter import *
import time
root = Tk()
root.title("Rk Gui") 
root.geometry("640x480+300+100") 
'''
progressbar = ttk.Progressbar(root,maximum = 100,mode = "determinate") # 결정되지 않고 계속움직임
progressbar.start(10) # 10ms 마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop() # 작동 중지

btn = Button(root,text="중지",command=btncmd)
btn.pack()
'''
p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum = 100, length=150,variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(101):
        time.sleep(0.01) #0.01초 시간지연

        p_var2.set(i) # progressbar의 값 설정
        progressbar2.update() # ui업데이트
        print(p_var2.get())

btn = Button(root,text="시작",command=btncmd2)
btn.pack()

root.mainloop() 
