from agent import Agent
import sqlite3


class Login_Controller(Agent):
    """searches through the inventory for user specific input"""

    def __init__(self):
        """default constructor"""
        super(Login_Controller, self).__init__("login_controller")
        self.valid_login = False

    def check_credentials(self):
        username = self.ask("main_manager", "username")
        password = self.ask("main_manager", "password")
        conn = sqlite3.connect('music_store.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT PASSWORD FROM EMPLOYEES WHERE USERNAME = ?""", (username,))
        correct_password = cursor.fetchone()
        if correct_password:
            if correct_password[0] == password:
                self.valid_login = True
        conn.close()