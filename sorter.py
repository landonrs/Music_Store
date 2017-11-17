from agent import Agent


class Sorter(Agent):
    """searches through the inventory for user specific input"""

    def __init__(self):
        """default constructor"""
        super(Sorter, self).__init__("sorter")