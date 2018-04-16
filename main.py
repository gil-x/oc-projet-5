from datamanager import DataManager
from apifisherman import ApiFisherman
from client import Client
from datetime import datetime

from config import *

class Main:
    """Just the main class."""
    def __init__(self):
        self.database = DataManager(USER, PASSWORD, HOST, DATABASE, CHARSET)
        self.fisher = ApiFisherman()
        self.client = Client(self.database)
        self.categories = CATEGORIES

    def build_data(self):
        self.database.build_db()
        print("Tables builded")
        self.database.add_category(self.categories)
        print("Added categories")
        products = self.fisher.get_products_from_api()
        self.database.add_subcategory(products)
        self.database.add_products(products)
        self.database.add_fulltext_index()
        self.client.mainmenu()

    def update_data(self):
        self.database.clean_products()
        # self.database.build_db()
        products = self.fisher.get_products_from_api()
        self.database.add_subcategory(products)
        self.database.add_products(products)
        # self.database.add_fulltext_index()
        self.client.mainmenu()

    def update_checker(self):
        current_time = str(datetime.now().timestamp())
        try:
            data_timestamp = open('data_timestamp.txt', 'r')
            if datetime.now().timestamp() - float(data_timestamp.readline()) > 86400:
                print("""
Datas are a bit old, I'm going to refresh all of this!
Please wait...
                """)
                self.update_data()
                data_timestamp = open('data_timestamp.txt', 'w')
                data_timestamp.write(current_time)
                data_timestamp.close()
            else:
                # print("I should run main now...")
                self.client.mainmenu()
        except FileNotFoundError:
            print("It seems to be your first use, let me some time to get some foods...")
            new_data_timestamp = open('data_timestamp.txt', 'w', encoding="utf-8")
            new_data_timestamp.write(current_time)
            new_data_timestamp.close()
            self.build_data()

    def run(self):
        self.update_checker()
        # self.database.clean_products()

main = Main()

main.run()
