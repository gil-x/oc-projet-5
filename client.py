from datamanager import DataManager

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
        chosen_category = input("your choice:\n")
        while int(chosen_category) not in range(1, len(main_categories)):
            print("Sorry, you have to choose a number between 1 and {}.".format(len(main_categories)))

        self.display_product(datamanager, chosen_category)

    def display_product(self, datamanager, category):
        # DEBUG:
        # print("category in display_product:", category)
        ramdom_products = datamanager.random_pick(10, category)
        for id, product in enumerate(ramdom_products):
            print("{}. {} ({} - cat: {})".format(id + 1, product["product_name"], product["grade"], product["category_id"]))

        self.ask_product_to_substitute(ramdom_products)

    def ask_product_to_substitute(self, ramdom_products):
        print("Which product to you want to subsitute?")
        chosen_product = input("your choice:\n")
        while int(chosen_product) not in range(1, len(ramdom_products)):
            print("Sorry, you have to choose a number between 1 and {}.".format(len(ramdom_products)))
        print("Your choice is:", ramdom_products[int(chosen_product) - 1])
        pass

    def display_favorites(self):
        pass

    def display_favorite(self):
        pass
