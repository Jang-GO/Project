import os
from tkinter import*

root=Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480+300+100")


filename = "mynote.txt"
def addfile():
    if os.path.isfile(filename):
        with open(filename,'r',encoding = 'utf8') as file:
            txt.delete("1.0",END) # 텍슽 위젯 본문 삭제
            txt.insert(END,file.read())

def savefile():
    with open(filename,"w",encoding='utf8') as file:
        file.write(txt.get("1.0",END)) # 모든내용을 가져와서 저장
menu=Menu()
menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label='열기',command=addfile)
menu_file.add_command(label='저장',command = savefile)
menu_file.add_separator()
menu_file.add_command(label='끝내기',command=root.quit)
menu.add_cascade(label='파일',menu=menu_file)

menu.add_cascade(label='편집')
menu.add_cascade(label='서식')
menu.add_cascade(label='보기')
menu.add_cascade(label='도움말')

#스크롤바 처리
scrollbar = Scrollbar(root)
scrollbar.pack(side="right",fill='y')

#본문영역 텍스트박스
txt = Text(root,yscrollcommand = scrollbar.set)
txt.pack(fill="both",expand=True,side='left')

scrollbar.config(command=txt.yview)

root.config(menu=menu) # 이게 있어야 메뉴들이 추가됨
root.mainloop()
