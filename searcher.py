from agent import Agent


class Searcher(Agent):
    """searches through the inventory for user specific input"""

    def __init__(self):
        """default constructor"""
        super(Searcher, self).__init__("searcher")

    def search(self):
        print("searching database")