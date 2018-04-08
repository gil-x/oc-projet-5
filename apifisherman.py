import requests
import pprint
import note

from config import *

class ApiFisherman:
    """This talk to the API, gets the """

    def __init__(self):
        pass

    def fish_category(self):
        args = {
            'action': "process",
            'tagtype_0': "categories",
            'tag_contains_0': "contains",
            'tag_0': "Seafood",
            'json': 1,
            # 'search_terms': "*",
            # 'category': 'Cheeses',
            # 'page_size': 10000,
            # 'search_simple': 1,
            # 'process': "process",
            }
        response = requests.get(ADV_API, params=args)

        monLog = note.Note('log.txt')
        requested = "URL:{} | status:{}".format(response.url, response.status_code)
        monLog.addLine(requested)

        response_json = response.json()["products"]
        products_total = (len(response_json))
        products_valids = []
        for p in response_json:
            try:
                product_ok = {k: v for k, v in p.items() if (k in [
                    "product_name_fr",
                    "code",
                    "url",
                    "categories",
                    "nutrition_grades",
                    "stores",
                    ] and v != "") }
                # printer = pprint.PrettyPrinter(indent=2)
                # printer.pprint(product_ok)
                # print("product_ok['stores']=", product_ok["stores"])
                products_valids.append(product_ok)
            except KeyError:
                pass
        print("Registered products: {}/{}.".format(len(products_valids), products_total))
        return products_valids
