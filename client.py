# from self.datamanager import self.datamanager

class Client:
    """Manage all displays, button, listings."""

    def __init__(self, datamanager):
        self.datamanager = datamanager
        self.chosen_category = ""
        self.ramdom_products = ""
        self.chosen_product = ""
        self.substitutes = ""

    def mainmenu(self):
        print("""
===================================
     Welcome in openfoodfacts!
===================================
1. Look for good food substitutes
2. See my favorites subsitutes
3. QUIT
        """)
        choice = self.get_choice("\n> What do you want to do?", 3)
        if choice == 1:
            self.ask_category()
        elif choice == 2:
            self.display_favorites()
        else:
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
        self.ramdom_products = self.datamanager.random_pick(
                10,
                self.chosen_category,
                )
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
        print("chosen_product_categories:", chosen_product_categories)
        self.substitutes = self.datamanager.find_substitutes(
                self.chosen_category,
                chosen_product_categories
                )
        self.roll_substitutes()


    def roll_substitutes(self):
        """
        Displays one by one each subsitute found
        Each step user can register it in favorite, see next, quit (using get_choice)
        """
        for product in self.substitutes:
            print("""
{} is a good subsitute to {}, you can see more about this product at {}
            """.format(
                    product["product_name"],
                    self.chosen_product["product_name"],
                    product["url"],
                    )
                )
            print("What do you want to do?")
            print(
"""
1. save product to my favorites and return to main menu
2. save product to my favorites and see more subsitutes
3. see next product
4. go to main menu
5. quit
""")
            response = self.get_choice("", 5)
            if response == 1:
                self.datamanager.add_favorite(product)
                self.mainmenu()
            elif response == 2:
                self.datamanager.add_favorite(product)
            elif response == 3:
                pass
            elif response == 4:
                self.mainmenu()
            elif response == 5:
                break


    def get_choice(self, question, choices_number):
        """
        - Capture user choice in input
        - waiting for a integer in specified range,
        - if not, ask again until response is fine.
        """
        print(question)
        while True:
            response = input("Your choice: ")
            try:
                if int(response) in range(1, choices_number + 1):
                    return int(response)
                else:
                    raise ValueError
            except (TypeError, ValueError):
                print("""
ERROR! You must pick a number between 1 and {}.""".format(choices_number))

    def display_favorites(self):
        """
        - Display list of favorite products from table Favorites
        - Each product has a number index,
        - User can choose a product to have more informations or quit (use get_choice)
        """
        pruducts = self.datamanager.get_favorites().as_dict()
        for id, product in enumerate(pruducts):
            print("{}. {}".format(id + 1, product["product_name"]))
        print("{}. RETURN TO MAIN MENU".format(len(pruducts) + 1))
        # pdb.set_trace()
        response = self.get_choice(
                "See details?",
                len(pruducts) + 1
            )
        if response == len(pruducts) + 1:
            self.mainmenu()
        else:
            self.display_favorite(pruducts[response - 1])

    def display_favorite(self, product):
        """
        - Display details from product
        - User can choose to return to favorites list or quit (use get_choice)
        """
        print("""
{}, (grade {})
- You can buy it at: {}
- See more at: {}
""".format(
        product["product_name"],
        product["grade"],
        product["store"],
        product["url"],
        ))
        print("""
1. Look for good food substitutes
2. Return to my favorites substitutes
3. QUIT
        """)
        choice = self.get_choice("\n> What do you want to do?", 3)
        if choice == 1:
            self.ask_category()
        elif choice == 2:
            self.display_favorites()
        else:
            pass
