# from datamanager import DataManager

class ClientUI:
    """Manage all displays, button, listings."""

    def __init__(self):
        pass

    def ask_to_wait(self):
        pass

    def ask_category(self, datamanager):
        print("Which category do you want to explore?")
        main_categories = datamanager.get_main_categories()
        for main_category in main_categories:
            print("{}. {}".format(main_category["id"], main_category["category_name"]))
        # for i in range(1, len(main_categories) + 1):
        #     print("range:", i)
        chosen_category = input("your choice:\n")
        while int(chosen_category) not in range(1, len(main_categories) + 1):
            print("Sorry, you have to choose a number between 1 and {}.".format(len(main_categories)))

        self.display_product(datamanager, chosen_category)

    def display_product(self, datamanager, chosen_category):
        # DEBUG:
        # print("category in display_product:", category)
        ramdom_products = datamanager.random_pick(10, chosen_category)
        for id, product in enumerate(ramdom_products):
            print("{}. {} ({} - cat: {})".format(id + 1, product["product_name"], product["grade"], product["category_id"]))

        self.ask_product_to_substitute(datamanager, chosen_category, ramdom_products)

    def ask_product_to_substitute(self, datamanager, chosen_category, ramdom_products):
        print("Which product to you want to subsitute?")
        chosen_product = input("your choice:\n")
        while int(chosen_product) not in range(1, len(ramdom_products) + 1):
            print("Sorry, you have to choose a number between 1 and {}.".format(len(ramdom_products)))
        print("Your choice is:", ramdom_products[int(chosen_product) - 1])
        chosen_product = ramdom_products[int(chosen_product) - 1]
        self.fetch_subsitute(datamanager, chosen_category, chosen_product)

    def fetch_subsitute(self, datamanager, chosen_category, chosen_product, ):
        chosen_product_categories = chosen_product["categories"]
        print(chosen_product_categories)
        for i in datamanager.find_substitutes(chosen_category, chosen_product_categories):
            print("{}. {}".format(i["product_name"], i["grade"]))
        pass

    def get_choice(self, question, response_range):
        response = input("your choice:\n")
        try:
            response = int(response)
        except TypeError:
            print("You have to pick a number between")
        while (response):
         pass


    def display_favorites(self):
        pass

    def display_favorite(self):
        pass
