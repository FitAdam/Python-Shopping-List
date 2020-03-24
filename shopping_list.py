import os.path
from datetime import date
from pymongo import MongoClient
from Order import Order
import csv


# This function adds products to the shopping list

def add_product():
    # Introduction
    print("\n You have chosen to add an order to the shopping list... \n")

    # Name the file with type of products
    category_of_products = "shopping list-categories.txt"
    if not os.path.exists(category_of_products):
        print("File does not exist!")
        with open(category_of_products, "w"):
            pass
        print("\nCreated a file in this directory named category_of_products.txt...")
        return
    # Open the category of products in write mode and read in the lines
    category_of_products = open(category_of_products, "r+")
    categories = category_of_products.readlines()

    # Name the list of orders
    list_of_orders = "shopping list-orders.txt"
    if not os.path.exists(list_of_orders):
        print("File shopping list-orders does not exist!")
        with open(list_of_orders, "w"):
            pass
        print("\nCreated a file in this directory named shopping list-orders.txt...")
        return
    # Open the shopping list file in write mode and read the lines
    list_of_orders = open(list_of_orders, "r+")
    list_of_orders = list_of_orders.read()
    if len(list_of_orders) == 0:
        print("You have no orders added!")

    # Check if the files has a categories written
    if len(categories) == 0:
        print("No categories added!")
        print("Check if you need to add one or more by editing the category_of_products.txt.")
        print("Every category must on a new line.")
        print("\nExiting...")
        return

    # the main loop

    while True:
        # Ask user for the input

        date_of_order = date.today().strftime("%B %d, %Y")
        product_name = input("What do you need to buy? ")
        # TODO check if the product was added
        
        quantity = input("Enter the quantity: ")

        # Choose the category of the product_name
        print("\nSelect the category of the product: ")
        index = 1
        for x in categories:
            print(str(index) + ". " + x.strip("\n"))
            index = index + 1
        category_index = input("")
        category = categories[int(category_index) - 1]

        # Summarize the order
        print("\nHere is your order summary:")
        print(" Date: " + date_of_order)
        print(" Product: " + product_name)
        print(" Amount: " + quantity)
        print(" Category: " + category)

        new_order = Order(product_name, date_of_order, quantity, category)

        # Ask whether to save the order
        record = input("\nSave this order?\n1 = Yes\n2 = No\n\n")
        if record == "1":
            with open('shopping list-orders.txt', 'a') as fd:
                fd.write(f'\n {new_order.product_name, new_order.date_of_order, new_order.quantity, new_order.category}')
            # TODO
            # save the object to your list
            # validate if it was saved before and add inform the user
            # user can add more or cancel 

            print("\nOrder recorded...")
            # If the user chose not to record the order
        else:
            print("\nOrder not recorded...")
            # Close the file and quit
            category_of_products.close()
            return

        option = input("\nWould you like to add another order?\n1 = Yes\n2 = No\n")
        if option == "2":
            break

        category_of_products.close()

def display_list():
   # This opens a file, mode "r = read only", encoding is for ?
    filen = open("shopping list-orders.txt", "r", encoding="utf-8")
    t = filen.read()
    print(t)
    return

def send_list():
    # TODO
    # This will send your list to email.
    return


# This is the main function

def main():
    # Welcome
    print("\nWelcome to your Interactive Shopping List!")

    # Forever
    while True:
        # Give the user options
        print()
        print("Choose an option:")
        print("1. Add an order")
        print("2. See your shopping list")
        print("3. Send your list to email")
        print("4. Exit")
        option = input("")
        # add new options in the future
        if option == "1":
            add_product()
        if option == "2":
            display_list()
        if option == "3":
            send_list()
        else:
            # Exit
            print("\nInteractive Shopping List!\n")
            break


if __name__ == "__main__":
    main()
