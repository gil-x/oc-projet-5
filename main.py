# import note

from datamanager import DataManager
from apifisherman import ApiFisherman
from config import *

class Main:
    """Just the main class."""
    def __init__(self):
        self.database = DataManager(USER, PASSWORD, HOST, DATABASE, CHARSET)
        self.fisher = ApiFisherman()
        self.categories = CATEGORIES

    def run(self):
        # self.database.delete_all_tables()
        # print("Database empty")
        self.database.build_db()
        print("Tables builded")
        self.database.add_category(self.categories)
        print("Added categories")
        while self.categories:
            category = self.categories.pop(0)
            print("category:", category)
            self.database.add_products(self.fisher.fetch_category(category), category)


main = Main()
main.run()
