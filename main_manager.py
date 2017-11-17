from agent import Agent
from inventory_editor import Inv_Editor
from log_in_controller import Login_Controller
from searcher import Searcher
from sorter import Sorter
from tkinter import *
from sqlite3 import *



class Main_Manager(Agent):
    """driver agent of the program, tells all other agents how to run the application"""

    def __init__(self, environment):
        """default constructor"""
        super(Main_Manager, self).__init__("main_manager", environment)
        self.inv_editor = Inv_Editor()
        self.login_controller = Login_Controller()
        self.searcher = Searcher()
        self.sorter = Sorter()

    def create_main_window(self):
        tk_library = Tk()
        tk_library.minsize(width=300, height=300)
        # create a menu
        main_menu = Menu(tk_library)
        tk_library.config(menu=main_menu)
        username_entry = Entry(tk_library)
        username_entry.insert(0, "Username")
        username_entry.place(x=100,y=100)
        password_entry = Entry(tk_library, show="*")
        password_entry.insert(0, "Password")
        password_entry.place(x=100, y=125)
        username_entry.focus_set()
        login_button = Button(tk_library, text="Login", command=self.login)
        login_button.config(width=15)
        login_button.place(x=100, y=150)

    def login(self):
        pass




boss = Main_Manager(None)
boss.create_main_window()
mainloop()
boss.searcher.search()


