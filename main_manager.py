from agent import Agent
from inventory_editor import Inv_Editor
from log_in_controller import Login_Controller
from searcher import Searcher
from sorter import Sorter
from tkinter import *
from main_menu import Main_Menu
import sqlite3


class Main_Manager(Agent):
    """driver agent of the program, tells all other agents how to run the application"""

    def __init__(self, environment):
        """default constructor"""
        super(Main_Manager, self).__init__("main_manager", environment)
        self.inv_editor = Inv_Editor()
        self.login_controller = Login_Controller()
        self.searcher = Searcher()
        self.sorter = Sorter()
        self.login_window = Tk()
        self.create_main_window()
        self.main_menu = None
        self.working = True
        self.username = ""
        self.password = ""
        self.initialize_DB()
        #self.main_loop = self.login_window.mainloop()

    def initialize_DB(self):
        conn = sqlite3.connect('music_store.db')
        cursor = conn.cursor()

        cursor.execute("""DROP TABLE IF EXISTS EMPLOYEES""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS EMPLOYEES
            (
             EMPLOYEE_ID INTEGER PRIMARY KEY ,
             USERNAME UNIQUE,
             PASSWORD
             )""")

        # insert first employee into DB
        cursor.execute("INSERT OR IGNORE INTO EMPLOYEES(username, password) VALUES('landonrs', 'music8')")
        cursor.execute("INSERT OR IGNORE INTO EMPLOYEES(username, password) VALUES('skwid8', 'yourfeesh8')")
        cursor.execute("SELECT * FROM EMPLOYEES")
        print(cursor.fetchall())
        conn.commit()
        conn.close()

    def create_main_window(self):
        self.login_window.minsize(width=300, height=300)
        # create a menu
        main_menu = Menu(self.login_window)
        self.login_window.config(menu=main_menu)
        username_entry = Entry(self.login_window)
        username_entry.insert(0, "Username")
        username_entry.place(x=100,y=100)
        password_entry = Entry(self.login_window, show="*")
        password_entry.insert(0, "Password")
        password_entry.place(x=100, y=125)
        username_entry.focus_set()
        login_button = Button(self.login_window, text="Login", command= lambda:self.login(username_entry.get(), password_entry.get()))
        login_button.config(width=15)
        login_button.place(x=100, y=150)

    def open_main_menu(self):
        print("opening menu")
        self.main_menu = Main_Menu()
        self.login_window.destroy()
        #self.main_loop = self.main_menu.mainloop()

    def login(self, username, password):
        self.username = username
        self.password = password
        self.login_controller.check_credentials()
        valid_login = self.ask("login_controller", "valid_login")
        if valid_login:
            self.open_main_menu()

boss = Main_Manager(None)
mainloop()



