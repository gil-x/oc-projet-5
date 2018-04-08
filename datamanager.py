import records
import pprint

class DataManager:
    """Read and write the database."""

    def __init__(self, user, password, host, database, charset="charset=utf8"):
        # self.db = records.Database('mysql+pymysql://sqgil:pass@localhost/off_0?charset=utf8')
        self.db = records.Database("mysql+pymysql://{}:{}@{}/{}?{}".format(
                user,
                password,
                host,
                database,
                charset)
                )

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

    def add_category(self, category):
        self.db.query("""
            INSERT INTO Category (name)
            VALUES(:name)
            """,
            name=category
            )

    def add_products(self, products):
        printer = pprint.PrettyPrinter(indent=2)
        for product in products:
            # printer.pprint(product)
            # print(type(product))
            # print("product_name_fr:", product["product_name_fr"])
            # print("nutrition_grades:", product["nutrition_grades"])
            # print("stores:", product["stores"])
            try:
                self.db.query("""
                    INSERT INTO Product (name, barcode, grade, url, store, category)
                    VALUES(:name, :barcode, :grade, :url, :store, :category)
                    """,
                    name=product["product_name_fr"],
                    barcode=product["code"],
                    grade=product["nutrition_grades"],
                    url=product["url"],
                    store=product["stores"],
                    category=1
                    )
                print("{} added.".format(product["product_name_fr"]))
            except KeyError:
                print("Key error")


        # self.db.query("""
        # INSERT INTO Product (name, barcode, grade, url, store, category)
        # VALUES(:name, :barcode, :grade, :url, :store, :category)
        # """,
        # # pk=pk,
        # name="name",
        # barcode="0123456789123",
        # grade="e",
        # url="url",
        # store="store",
        # category=1
        # )






    def clean_products(self):
        self.db.query("""
        DELETE FROM Product
        WHERE grade IN ("D", "E")
        )
        ENGINE=INNODB;
        """)

    # def delete_all_tables(self):
    #     self.db.query("""
    #     DROP TABLE Category;
    #     """)



#
#         CREATE TABLE Animal (
#             id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
#             espece VARCHAR(40) NOT NULL,
#             sexe CHAR(1),
#             date_naissance DATETIME NOT NULL,
#             nom VARCHAR(30),
#             commentaires TEXT,
#             PRIMARY KEY (id)
#         )
#         ENGINE=INNODB;
#
#
#
#
#
# class DatabaseManager(self):
#     def __init__(self):
#
#
# db.query("""
# CREATE TABLE IF NOT EXISTS Product (
#     id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
#     name VARCHAR(100) NOT NULL,
#     barcode CHAR(13) NOT NULL,
#     grade CHAR(1) NOT NULL,
#     url VARCHAR(255) NOT NULL,
#     store VARCHAR(255) NOT NULL,
#     PRIMARY KEY (id)
# )
# ENGINE=INNODB;
# """)
#
#
# db = records.Database('mysql+pymysql://sqgil:pass@localhost/off_0?charset=utf8')
