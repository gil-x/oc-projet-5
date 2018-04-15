import requests
import pprint
import note

from config import *

class ApiFisherman:
    """This class talk to the OFF api, gets the stuff."""

    def __init__(self):
        pass

    # récupérer spécifiquement des A B D et E
    def fetch_category(self, category):
        # print("category in fetch_category:", category)
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
                # DEBUG
                products_valids.append(product_ok)
            except KeyError:
                pass

        print("Registered products: {}/{}.".format(len(products_valids), products_total))
        return products_valids
