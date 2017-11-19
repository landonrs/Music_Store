from agent import Agent
import sqlite3


class Searcher(Agent):
    """searches through the inventory for user specific input"""

    def __init__(self):
        """default constructor"""
        super(Searcher, self).__init__("searcher")

    def search(self, search_word, filter_word):
        column_name = ""
        if filter_word == "Type":
            column_name = "ITEM_TYPE"
        elif filter_word == "Make":
            column_name = "ITEM_MAKE"
        elif filter_word == "Model":
            column_name = "ITEM_MODEL"

        connection = sqlite3.connect("music_store.db")
        cursor = connection.cursor()
        statement = "SELECT * FROM INVENTORY WHERE " + column_name + " = '" + search_word + "'"

        cursor.execute(statement)
        print(cursor.fetchall())
        connection.close()
