from tkinter import *

root = Tk()
root.title("Rk Gui") # 상단 타이틀 제목
root.geometry("640x480+300+100")
btn1 = Button(root, text="버튼1")
btn1.pack()

btn2=  Button(root,padx=5,pady=10,text = "버튼2 입니 다람쥐") #padx,y : 텍스트기준 여백 설정
btn2.pack()

btn3=  Button(root,padx=10,pady=5,text = "버튼3")
btn3.pack()

btn4 = Button(root, width=10,height=3,text = '버튼4ㅌㅋㅌㅋㅌㅋ') # width,height : 버튼 크기 고정
btn4.pack()

btn5 = Button(root, fg='red',bg='yellow',text='버튼5')
btn5.pack()

photo = PhotoImage(file='gui_basic/img.png')
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print('버튼이 클릭되었습니다.')

btn7 = Button(root, text = '동작하는버튼',command=btncmd)
btn7.pack()

root.mainloop() # 창이 닫히지 않도록해줌

