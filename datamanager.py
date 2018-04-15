import records
import pprint

from config import *

class DataManager:
    """Read and write the database."""

    def __init__(self, user, password, host, database, charset="charset=utf8mb4"):
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
            category_name VARCHAR(100) NOT NULL,
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
            product_name VARCHAR(100) NOT NULL,
            barcode CHAR(13) NOT NULL,
            grade CHAR(1) NOT NULL,
            url VARCHAR(255) NOT NULL,
            store VARCHAR(255),
            categories VARCHAR(255),
            category_id SMALLINT UNSIGNED NOT NULL,
            -- favorite CHAR(1) NOT NULL,
            CONSTRAINT fk_cat_product
                FOREIGN KEY (category_id)
                REFERENCES Category(id),
            PRIMARY KEY (id)
        )
        ENGINE=INNODB;
        """)

        # The favorites products, grade A or B
        self.db.query("""
        CREATE TABLE IF NOT EXISTS Favorite (
            id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
            product_name VARCHAR(100) NOT NULL,
            barcode CHAR(13) NOT NULL,
            grade CHAR(1) NOT NULL,
            url VARCHAR(255) NOT NULL,
            store VARCHAR(255),
            categories VARCHAR(255),
            category_id SMALLINT UNSIGNED NOT NULL,
            CONSTRAINT fk_cat_favorite
                FOREIGN KEY (category_id)
                REFERENCES Category(id),
            PRIMARY KEY (id)
        )
        ENGINE=INNODB;
        """)

    def add_category(self, categories):
        for category in categories:
            self.db.query("""
                INSERT INTO Category (category_name)
                VALUES(:category_name)
                """,
                category_name=category
                )

    def add_products(self, products, category):
        # DEBUG:
        printer = pprint.PrettyPrinter(indent=2)
        total_products = len(products)
        valid_products = 0

        for product in products:
            # print("self.categories:", self.categories)
            try:
                self.db.query("""
                    INSERT INTO Product (product_name, barcode, grade, url, store, category_id, categories)
                    VALUES(:product_name, :barcode, :grade, :url, :store, :category_id, :categories)
                    """,
                    product_name=product["product_name_fr"],
                    barcode=product["code"],
                    grade=product["nutrition_grades"],
                    url=product["url"],
                    store=product["stores"],
                    categories=product["categories"],
                    category_id=self.categories.index(category) + 1
                    )
                # print("{} added.".format(product["product_name_fr"]))
                valid_products += 1
            except KeyError:
                print("Key error")

        print("Registered products: {}/{}".format(valid_products, total_products))

    def add_favorite(self, product):
        self.db.query("""
            INSERT INTO Favorite (product_name, barcode, grade, url, store, category_id, categories)
            VALUES(:product_name, :barcode, :grade, :url, :store, :category_id, :categories)
            """,
            product_name=product["product_name"],
            barcode=product["barcode"],
            grade=product["grade"],
            url=product["url"],
            store=product["store"],
            categories=product["categories"],
            category_id=product["category_id"]
            )

    def random_pick(self, number, category):
        # DEBUG:
        # print("category arg in random_pick:", category, type(category))
        # category_arg= int(category)
        return self.db.query("""
            SELECT *
            FROM Product
            INNER JOIN Category
                ON Product.category_id = Category.id
            WHERE grade = "e"
                -- AND category_id = 2
                AND Category.id = {}
            ORDER BY RAND()
            LIMIT 10;
            """.format(category),
            # category_arg= int(category)
            )


    def get_main_categories(self):
        return self.db.query("""
            SELECT * FROM Category;
            """,
            )

    def get_favorites(self):
        return self.db.query("""
            SELECT *
            FROM Favorite
        """)

    def add_fulltext_index(self):
        self.db.query("""
        ALTER TABLE Product
        ADD FULLTEXT ind_categories (categories);
        """
        )

    def find_substitutes(self, chosen_category, chosen_product_categories):
        return self.db.query("""
            SELECT *
            FROM Product
            WHERE
            category_id = :chosen_category
            AND (grade = 'a' OR grade = 'b')
            AND MATCH categories
            AGAINST (:chosen_product_categories)
            LIMIT 5;
            """,
            chosen_category= chosen_category,
            chosen_product_categories= chosen_product_categories
            )



    def clean_products(self):
        self.db.query("""
        DROP TABLE Product;
        """)
