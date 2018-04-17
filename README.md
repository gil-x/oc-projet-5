# Parcours développeur d'application Python - Projet 5

This small Python application provide a simple use of openfoodfacts API.

## Get started

1. create a database (mysql is fine) and replace the fields (user, pass...) in config.py
2. build and activate the venv according to the requirements (see Python documentation to do it)
3. execute main.py

## Fetch some good food

You can navigate into shell menus to do the following tasks:
- choose a main category
- then choose a product
- the application will find 5 subsitutes, displaying one by one
- you can choose each each time to register, see next, or quit

## Look at your saved products
- at main menu you can choose 'see my favorites'
- the application show you a complete list of your saved products
- you can enter the id of a saved product to see more about it, or quit

## Important
- at first use, the application will go fetch products in OFF, this may take a few time (do not quit!)
- a data_timestamp file will be created, beware to not remove it!
- each time you launch the application, data_timestamp is used to check if datas are more than 72 hours old, in this case, the application will rebuild the pool of products (not your favorites!)
- the data_timestamp file is very important, do not remove it unless your want to clean the installation (then you should erase all tables in database)

## More custom
- Maybe you use to eat another type of food, not only cheese or salted snacks? That's a good point! Feel free to change the list of CATEGORIES in config.py, according to the correct labels used in openfoodfacts.
