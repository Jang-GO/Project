from tkinter import *

root = Tk()
root.title("Rk Gui") 
root.geometry("640x480+300+100") 

def create_new_file():
    print("새파일을 만듭니다")

menu = Menu(root)

menu_file = Menu(menu,tearoff = 0)
menu_file.add_command(label='New file',command=create_new_file)
menu_file.add_command(label ='New Window')
menu_file.add_separator()
menu_file.add_command(label='Open File')
menu_file.add_separator()
menu_file.add_command(label='Save all',state = 'disable') # 비활성화
menu_file.add_separator()
menu_file.add_command(label='Exit',command = root.quit)
menu.add_cascade(label ='File',menu=menu_file)

#Edit메뉴(빈값)
menu.add_cascade(label = 'Edit')

#Languege 메뉴 추가(radio버튼을 통해서 택1)
menu_lang = Menu(menu,tearoff=0)
menu_lang.add_radiobutton(label = 'python')
menu_lang.add_radiobutton(label = 'Java')
menu_lang.add_radiobutton(label = 'C++')
menu.add_cascade(label='Languege',menu=menu_lang)

#View 메뉴
menu_view = Menu(menu,tearoff=0)
menu_view.add_checkbutton(label='Show Minimap')
menu.add_cascade(label='View',menu=menu_view)

root.config(menu=menu)
root.mainloop()
