import records
import pprint

from config import *

class DataManager:
    """Read and write the database."""

    def __init__(self, user, password, host, database, charset="charset=utf8"):
        self.db = records.Database("mysql+pymysql://{}:{}@{}/{}?{}".format(
                user,
                password,
                host,
                database,
                charset)
                )
        # self.categories = CATEGORIES
        self.categories = ["Salty snacks", "Cheeses", "Beverage", "Sauces", "Biscuits"]

    def build_db(self):
        """Create the tables."""

        # The products categories
        self.db.query("""
        CREATE TABLE IF NOT EXISTS Category (
            id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            PRIMARY KEY (id)
        )
        ENGINE=INNODB;
        """)

        # The pool of products of grade A, B and E.
        # AJOUTER LES CALORIES !!!
        # AJOUTER LES CALORIES !!!
        # AJOUTER LES CALORIES !!!
        self.db.query("""
        CREATE TABLE IF NOT EXISTS Product (
            id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            barcode CHAR(13) NOT NULL,
            grade CHAR(1) NOT NULL,
            url VARCHAR(255) NOT NULL,
            store VARCHAR(255),
            categories VARCHAR(255),
            category SMALLINT UNSIGNED NOT NULL,
            -- favorite CHAR(1) NOT NULL,
            CONSTRAINT fk_cat_product
                FOREIGN KEY (category)
                REFERENCES Category(id),
            PRIMARY KEY (id)
        )
        ENGINE=INNODB;
        """)

        # The favorites products, grade A or B
        self.db.query("""
        CREATE TABLE IF NOT EXISTS Favorite (
            id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            barcode CHAR(13) NOT NULL,
            grade CHAR(1) NOT NULL,
            url VARCHAR(255) NOT NULL,
            store VARCHAR(255),
            category SMALLINT UNSIGNED NOT NULL,
            CONSTRAINT fk_cat_favorite
                FOREIGN KEY (category)
                REFERENCES Category(id),
            PRIMARY KEY (id)
        )
        ENGINE=INNODB;
        """)

    def add_category(self, categories):
        for category in categories:
            self.db.query("""
                INSERT INTO Category (name)
                VALUES(:name)
                """,
                name=category
                )

    def add_products(self, products, category):

        # DEBUG:
        printer = pprint.PrettyPrinter(indent=2)
        total_products = len(products)
        valid_products = 0

        for product in products:
            print("self.categories:", self.categories)
            try:
                self.db.query("""
                    INSERT INTO Product (name, barcode, grade, url, store, category, categories)
                    VALUES(:name, :barcode, :grade, :url, :store, :category, :categories)
                    """,
                    name=product["product_name_fr"],
                    barcode=product["code"],
                    grade=product["nutrition_grades"],
                    url=product["url"],
                    store=product["stores"],
                    categories=product["categories"],
                    category=self.categories.index(category) + 1
                    )
                print("{} added.".format(product["product_name_fr"]))
                valid_products += 1
            except KeyError:
                print("Key error")

        print("Registered products: {}/{}".format(valid_products, total_products))

    def random_pick(self, number, category):
        pass


    def clean_products(self):
        self.db.query("""
        DELETE FROM Product
        WHERE grade IN ("D", "E")
        )
        ENGINE=INNODB;
        """)
