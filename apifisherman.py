import requests
import pprint
import note

from config import *

class ApiFisherman:
    """This class talk to the OFF api, gets the stuff."""

    def __init__(self):
        self.categories = CATEGORIES
        self.grades = ['a', 'b', 'd', 'e']


    def get_products_from_api(self):
        products_valids = {}
        products_total = 0
        for category in self.categories:
            products_in_category = []
            print("Looking for {}...". format(category))
            for grade in self.grades:
                args = {
                    'action': "process",
                    'tagtype_0': "categories",
                    'tag_contains_0': "contains",
                    'tag_0': category,
                    'nutrition_grades': grade,
                    'json': 1,
                    'page_size': 1000,
                    }
                response = requests.get(ADV_API, params=args)
                response_json = response.json()["products"]
                products_total += (len(response_json))
                required_keys = [
                    "product_name_fr",
                    "code",
                    "url",
                    "categories",
                    "nutrition_grades",
                    "stores",
                    ]
                for p in response_json:
                    try:
                        product_ok = {k:p[k] for k in required_keys}
                        products_in_category.append(product_ok)
                    except KeyError:
                        pass
            products_valids[category] = products_in_category
        print("Registered products: {}/{}.".format(len(products_valids), products_total))
        return products_valids




    def fetch_category(self, category):
        args = {
            'action': "process",
            'tagtype_0': "categories",
            'tag_contains_0': "contains",
            'tag_0': category,
            'json': 1,
            'page_size': 1000,
            }
        response = requests.get(ADV_API, params=args)

        monLog = note.Note('log.txt')
        requested = "URL:{} | status:{}".format(response.url, response.status_code)
        monLog.addLine(requested)

        response_json = response.json()["products"]

        # DEBUG
        products_total = (len(response_json))
        products_valids = []

        required_keys = [
            "product_name_fr",
            "code",
            "url",
            "categories",
            "nutrition_grades",
            "stores",
            ]

        for p in response_json:
            try:
                product_ok = {k:p[k] for k in required_keys}
                products_valids.append(product_ok)
            except KeyError:
                pass

        print("Registered products: {}/{}.".format(len(products_valids), products_total))
        return products_valids
