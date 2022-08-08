from tkinter import *

root = Tk()
root.title("Rk Gui") # 상단 타이틀 제목
root.geometry("640x480+300+100")

label1 = Label(root,text = '안녕하세요!')
label1.pack()

photo = PhotoImage(file='gui_basic/img.png')
label2= Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요!")

    global photo2 # Garbage Collection 때문에 전역변수로 선언해야 함수가끝나도 안없어짐
    photo2 = PhotoImage(file='gui_basic/img2.png')
    label2.config(image=photo2)

btn = Button(root,text='클릭',command = change)
btn.pack()

root.mainloop() # 창이 닫히지 않도록해줌
