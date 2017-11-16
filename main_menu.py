from tkinter import *

def callback():
    print("called the callback!")

tk_library = Tk()

# create a menu
main_menu = Menu(tk_library)
tk_library.config(menu=main_menu)

filemenu = Menu(main_menu)
main_menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=callback)
filemenu.add_command(label="Open...", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=callback)

helpmenu = Menu(main_menu)
main_menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=callback)

edit = Menu(main_menu)
main_menu.add_cascade(label="Edit", menu=edit)
edit.add_command(label="undo", command=callback)

b = Button(tk_library, text="OK", command=callback)
b.pack()

mainloop()

