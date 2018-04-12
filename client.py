# from self.datamanager import self.datamanager

class ClientUI:
    """Manage all displays, button, listings."""

    def __init__(self, datamanager):
        self.datamanager = datamanager
        self.chosen_category = ""
        self.ramdom_products = ""
        self.chosen_product = ""

    def mainmenu(self):
        print("""
===================================
     Welcome in openfoodfacts!
===================================
1. Look for good food find_substitutes
2. See my favorites subsitutes
        """)
        choice = self.get_choice("\n> What do you want to do?", 2)
        if choice == 1:
            self.ask_category()
        else:
            pass

    def ask_to_wait(self):
        pass

    def ask_category(self):

        main_categories = self.datamanager.get_main_categories()
        for main_category in main_categories:
            print("{}. {}".format(
                    main_category["id"],
                    main_category["category_name"],
                    )
                )
        self.chosen_category = self.get_choice(
            "\n> Which category do you want to explore?",
            len(main_categories))
        self.display_product()

    def display_product(self):
        self.ramdom_products = self.datamanager.random_pick(10, self.chosen_category)
        for id, product in enumerate(self.ramdom_products):
            print("{}. {} ({} - cat: {})".format(
                    id + 1,
                    product["product_name"],
                    product["grade"],
                    product["category_id"],
                    )
                )
        self.ask_product_to_substitute()

    def ask_product_to_substitute(self):
        self.chosen_product = self.get_choice(
            "\n> Which product to you want to subsitute?",
            10)
        self.chosen_product = self.ramdom_products[self.chosen_product - 1]
        self.fetch_subsitute()

    def fetch_subsitute(self):
        chosen_product_categories = self.chosen_product["categories"]
        substitutes = self.datamanager.find_substitutes(self.chosen_category, chosen_product_categories)
        for id, product in enumerate(substitutes):
            print("{}. {}. {}".format(
                    id + 1,
                    product["product_name"],
                    product["grade"],
                    )
                )

    def get_choice(self, question, choices_number):
        print(question)
        while True:
            response = input("Your choice: ")
            try:
                if int(response) in range(1, choices_number + 1):
                    return int(response)
                else:
                    raise ValueError
            except (TypeError, ValueError):
                print("X You have to pick a number between 1 and {}.".format(choices_number))



    def display_favorites(self):
        pass

    def display_favorite(self):
        pass
