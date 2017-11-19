from agent import Agent
import sqlite3


class Inv_Editor(Agent):
    """searches through the inventory for user specific input"""

    def __init__(self):
        """default constructor"""
        super(Inv_Editor, self).__init__("inv_editor")

    @staticmethod
    def add_item(type, make, model, price, image):
        connection = sqlite3.connect("music_store.db")
        cursor = connection.cursor()

        cursor.execute("""INSERT INTO INVENTORY(ITEM_TYPE, ITEM_MAKE, ITEM_MODEL, ITEM_PRICE, ITEM_IMAGE)
                        VALUES(?,?,?,?,?)""", (type, make, model, price, image))
        cursor.execute("""SELECT * FROM INVENTORY WHERE ITEM_TYPE = ?""", (type,))
        print(cursor.fetchall())

        connection.commit()
        connection.close()