from tkinter import *

root = Tk()
root.title("Rk Gui") 
root.geometry("640x480+300+100") 

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right',fill = 'y')

#set이 없으면 스크롤을 내려도 다시올라옴
listbox = Listbox(frame, selectmode = 'extend',height = 10, yscrollcommand = scrollbar.set)
for i in range(1,31):
    listbox.insert(END,str(i)+"일")
listbox.pack(side='left')

scrollbar.config(command=listbox.yview)

root.mainloop()
