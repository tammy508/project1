# custom order form for online business
import json
from pprint import pprint 
from pymongo import MongoClient 
from datetime import datetime

client = MongoClient()

db = client.project1

customers = db.customers

# f = open("customers.json", "r")
# list_cust = json.load(f)
# customers.insert_many(list_cust)
# f.close()

inventory = db.inventory

# f = open("inventory.json", "r")
# list_invent = json.load(f)
# inventory.insert_many(list_invent)
# f.close()

orders = db.orders

# f = open("orders.json", "r")
# list_ord = json.load(f)
# orders.insert_many(list_ord)
# f.close()

class Customer:
    def __init__(self, email, first_name, last_name, address):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

# prompt user to create new order or interact with orders
def menu():
    print("Hello, welcome to the custom order interface! Please select an item from the menu: ")
    print("\ta) Create new custom order")
    print("\tb) Cancel order")
    print("\tc) Look up past orders")
    print("\td) Update customer info")
    print("\te) Exit the interface")
    
    # direct user choice to appropriate menu item
    while True:
        item = input()

        if item != "a" and item != "b" and item != "c" and item != "d" and item != "e":
            print("I'm sorry, that is an invalid input. Please try again.")
            continue

        if item == "a":
            order()
        elif item == "b":
            cancel()
        elif item == "c":
            look_up()
        elif item == "d":
            modify()
        else:
            exit()
        break

##########################################################################################################

# beginning of creating a new order
def order():
    print("Welcome to a new order form")
    print("Email Address: ")
    email = input()
    # if email exists, skip to item
    if customers.count_documents({"email": email}) >= 1:
        print("Welcome back!")
        
    else:
        print("First Name: ")
        first_name = input()
        print("Last Name: ")
        last_name = input()
        print("Shipping Address: ")
        address = input()
        new_customer(email, first_name, last_name, address)

    print("Item to be customized: ")
    # check to see if item in available to be customized
    while True:
        item = input()
        if inventory.count_documents({"item_name": item}) == 0:
            print("The item is not in stock. Please try again.")
            continue
        else:
            break

    print("Enter customization: ")
    custom = input()

    while True:
        try:
            print("Enter quantity: ")
            quantity = int(input())
            break
        except ValueError:
            print("You must enter a number. Try again.")

    cost = get_cost(item, quantity)
    new_order(email, item, custom, quantity, cost)

    print("Thank you for your order!")

##########################################################################################################

# create new customer document in database
def new_customer(email, first_name, last_name, address):
    new_cust = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "address": address}
    customers.insert_one(new_cust)

# create new order document in database
def new_order(email, item, custom, quantity, cost):
    new_ord = {
        "email": email,
        "item": item,
        "customization": custom,
        "quantity": quantity,
        "cost": cost,
        "date_ordered": datetime.now()}
    orders.insert_one(new_ord)

# find the total cost of the items ordered
def get_cost(item, quantity):
    for i in inventory.find({"item_name" : item}):
        i_price = i.get("price") * quantity
        print("The total cost of your order is $" + i_price)
        return i_price

##########################################################################################################

# search for orders and cancel most recent order
def cancel():
    print("Enter your email address: ")
    while True:
        email = input()

        if orders.count_documents({"email": email}) == 0:
            print("There are no past orders associated with this email. Please try again.")
            continue
        else: 
            for e in orders.find({"email" : email}, {"_id":0}).sort("date_ordered", -1):
                pprint(e, sort_dicts=False)
        break
    print("You can only cancel your most recent order. Would you like to continue? y or n")
    while True:
        answer = input()
        if answer != "y" and answer != "n":
            print("I'm sorry, that is an invalid input. Please try again.")
            continue
        elif answer == "y":
            print("Your most recent order will be cancelled. Thank you for being a customer!")
            orders.find_one_and_delete({"email": email}, sort=[('date_ordered', -1)])
            break
        else:
            exit()

# find order history of user and give output in file
def look_up():
    print("Enter your email address: ")
    while True:
        email = input()
        found = []

        if orders.count_documents({"email": email}) == 0:
            print("There are no past orders associated with this email. Please try again.")
            continue
        else:
            for e in orders.find({"email" : email}, {"_id":0}):
                print("Your order history has been saved in a file for you.")
                found.append(e)
        break

    with open('past_orders.json', 'w') as outfile:
       json.dump(found, outfile, indent=4, default = str)

    outfile.close()

# allow users to modify their information
def modify():
    print("Enter your email address: ")
    while True:
        email = input()
        if customers.count_documents({"email": email}) == 0:
            print("There are no customers associated with this email. Please try again.")
            continue
        else:
            print("What would you like to modify?")
            print("\ta) Email")
            print("\tb) First Name")
            print("\tc) Last Name")
            print("\td) Address")
            
            while True:
                choice = input()

                if choice != "a" and choice != "b" and choice != "c" and choice != "d":
                    print("I'm sorry, that is an invalid input. Please try again.")
                    continue

                if choice == "a":
                    print("Enter your new email address: ")
                    newe = input()
                    customers.update_one({"email": email},{"$set": {"email": newe}})
                elif choice == "b":
                    print("Enter your new first name: ")
                    newf = input()
                    customers.update_one({"email": email},{"$set": {"first_name": newf}})
                elif choice == "c":
                    print("Enter your new last name: ")
                    newl = input()
                    customers.update_one({"email": email},{"$set": {"last_name": newl}})
                elif choice == "d":
                    print("Enter your new address: ")
                    newa = input()
                    customers.update_one({"email": email},{"$set": {"address": newa}})
                break
        break
    print("Your changes have been saved!")


menu()