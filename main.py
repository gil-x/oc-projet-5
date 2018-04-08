# import note

from datamanager import DataManager
from apifisherman import ApiFisherman
from config import *

class Main:
    """Just the main class."""
    def __init__(self):
        self.database = DataManager(USER, PASSWORD, HOST, DATABASE, CHARSET)
        self.fisher = ApiFisherman()

    def run(self):
        # self.database.delete_all_tables()
        # print("Database empty")
        self.database.build_db()
        print("Tables builded")
        self.database.add_category("Cheeses")
        print("Added spam category")
        self.database.add_products(self.fisher.fish_category())


main = Main()
main.run()
