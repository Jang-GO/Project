from tkinter import *

root = Tk()
root.title("Rk Gui") 
root.geometry("640x480+300+100") 

listbox = Listbox(root, selectmode = "extended",height=3) # height : 지정 개수만 보여줌 (0은 전부다)
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END,"수박") #END: 맨뒤에 추가
listbox.insert(END,"포도") 
listbox.pack()

def btncmd():
    #삭제
    #listbox.delete(0)

    #갯수 확인
    #print("리스트에는",listbox.size(),"개가 있어요")

    #항목 확인(시작idx,끝idx)
    #print("1~3번째 까지의 항목 = ",listbox.get(0,2))

    #선택된 항목 확인(인덱스로 반환(ex) (1,2,3))
    print("선택한 항목 = ",listbox.curselection())
btn = Button(root,text="클릭",command=btncmd)
btn.pack()

root.mainloop() 