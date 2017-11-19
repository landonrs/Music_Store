from agent import Agent
from inventory_editor import Inv_Editor
from log_in_controller import Login_Controller
from searcher import Searcher
from sorter import Sorter
import tkinter as tk
from tkinter import font as tkfont
from tkinter import Entry
from tkinter import Button
from tkinter import messagebox
from tkinter import END
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
        self.username_entry = None
        self.password_entry = None
        self.main_menu = Main_Menu()
        self.working = True
        self.username = ""
        self.password = ""
        self.initialize_DB()

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

    def open_main_menu(self):
        print("opening menu")
        self.main_menu.show_frame("StartPage")

    def login(self, username, password):
        self.username = username
        self.password = password
        self.login_controller.check_credentials()
        valid_login = self.ask("login_controller", "valid_login")
        if valid_login:
            self.open_main_menu()
        else:
            self.main_menu.display_login_error()

class Main_Menu(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.minsize(height="300", width="500")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, SearchPage, InsertPage, LoginPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def display_login_error(self):
        messagebox.showerror("Incorrect login", "Username or password is incorrect, please try again.")


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x")

        button1 = tk.Button(self, text="Go to Search Page",
                            command=lambda: controller.show_frame("SearchPage"))
        button2 = tk.Button(self, text="Add items to Inventory",
                            command=lambda: controller.show_frame("InsertPage"))
        button1.pack()
        button2.pack()


class SearchPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Search page", font=controller.title_font)
        label.pack(side="top", fill="x")

        button1 = tk.Button(self, text="return to main menu",
                            command=lambda: controller.show_frame("StartPage"))

        button1.pack()


class InsertPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Insert page", font=controller.title_font)
        label.pack(side="top", fill="x")
        item_name = Entry(self)
        item_name.place(x=100, y=100)
        name = tk.Label(self, text="name:")
        name.place(x=70, y=100)

        button1 = tk.Button(self, text="return to main menu",
                            command=lambda: controller.show_frame("StartPage"))
        button1.place(x=150, y=200)


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Employee Login", font=controller.title_font)
        label.pack(side="top", fill="x")
        username_entry = Entry(self)
        username_entry.insert(0, "landonrs")
        username_entry.place(x=100, y=100)
        password_entry = Entry(self, show="*")
        password_entry.insert(0, "music8")
        password_entry.place(x=100, y=125)
        username_entry.focus_set()
        login_button = Button(self, text="Login",
                              command=lambda: boss.login(username_entry.get(), password_entry.get()))
        login_button.config(width=15)
        login_button.place(x=100, y=150)



boss = Main_Manager(None)
boss.main_menu.mainloop()