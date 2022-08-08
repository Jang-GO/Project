from tkinter import *

root = Tk()
root.title("Rk Gui") 
root.geometry("640x480+300+100") 

txt = Text(root, width=30, height=5) #텍스트 위젯 생성
txt.pack()
txt.insert(END,"글자를 입력하세요") # END:글자를 어디에 넣을건지

e = Entry(root,width = 30) #엔트리에서는 엔터 입력불가능
e.pack()
e.insert(0,"한줄만 입력하세요")
'''
여러줄입력이 필요할땐 텍스트
엔트리는 한줄입력(엔터x) ex)로그인아이디 닉네임등등을 받을때 사용
'''
def btncmd():
    #내용출력
    print(txt.get("1.0",END)) # 1.0 : 라인1 부터,column 기준 0번째 인덱스부터 가져와라 END까지
    print(e.get())
    
    #내용삭제
    txt.delete("1.0",END)
    e.delete(0,END)
    
btn = Button(root,text="클릭",command=btncmd)
btn.pack()

root.mainloop() 