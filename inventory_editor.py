from agent import Agent


class Inv_Editor(Agent):
    """searches through the inventory for user specific input"""

    def __init__(self):
        """default constructor"""
        super(Inv_Editor, self).__init__("inv_editor")