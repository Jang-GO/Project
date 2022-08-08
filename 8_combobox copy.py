import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Rk Gui") 
root.geometry("640x480+300+100") 

values=[str(i) + '일' for i in range(1,32)] # 1~31까지의 숫자
combobox= ttk.Combobox(root, height=5, values=values)
combobox.set('카드 결제일') # 최초 목록 제목 설정
combobox.pack()

readonly_combobox= ttk.Combobox(root, height=10, values=values,state = "readonly")
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())
    
btn = Button(root,text="선택",command=btncmd)
btn.pack()

root.mainloop() 