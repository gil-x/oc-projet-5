# import note

from datamanager import DataManager
from apifisherman import ApiFisherman
from client import ClientUI

from config import *

class Main:
    """Just the main class."""
    def __init__(self):
        self.database = DataManager(USER, PASSWORD, HOST, DATABASE, CHARSET)
        self.fisher = ApiFisherman()
        self.client = ClientUI()
        self.categories = CATEGORIES

    def run(self):
        # self.database.build_db()
        # print("Tables builded")
        # self.database.add_category(self.categories)
        # print("Added categories")
        # while self.categories:
        #     category = self.categories.pop(0)
        #     print("category:", category)
        #     self.database.add_products(self.fisher.fetch_category(category), category)

        # self.database.get_main_categories()
        self.client.ask_category(self.database)

main = Main()
main.run()
