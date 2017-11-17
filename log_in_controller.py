from agent import Agent


class Login_Controller(Agent):
    """searches through the inventory for user specific input"""

    def __init__(self):
        """default constructor"""
        super(Login_Controller, self).__init__("login_controller")