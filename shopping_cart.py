# shopping_cart.py
from datetime import datetime
import dotenv
import os
from dotenv import load_dotenv


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output


#
# Information Input
#


now = datetime.now()
dt_string = now.strftime("%B %d, %Y %H:%M")


total_price = 0
selected_items = []


while True:  
    try:
        selected_item = input("Please input Product ID (1-20 is valid), when finished, enter 'DONE':")
        selected_item = selected_item.upper()
        if selected_item == "DONE":
            break
        elif 1 <= int(selected_item) <= 20:
            selected_items.append(selected_item)      
        else:
            raise ValueError()
    except ValueError:
        print("please enter a valid input")




#
# Information Output
#

print("---------------------")
print("CORNER GROCERY")
print("www.cornergrocerydc.com")
print("---------------------")
print(dt_string)
print("---------------------")
print("PRODUCTS PURCHASED:")

for selected_id in selected_items:
    matching_products = [item for item in products if str(item["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    print(matching_product["name"] + " ..." + to_usd(matching_product["price"]))

load_dotenv()

tax = os.getenv("TAX_RATE", default = .07)
tax = float(tax)

tax_dollars = tax * total_price
amount_due = total_price + tax_dollars

print("---------------------")
print("SUBTOTAL:" + to_usd(total_price))
print("TAX:" + to_usd(tax_dollars))
print("TOTAL:" + to_usd(amount_due))  
print("---------------------")
print("THANK YOU FOR SHOPPING WITH US, SEE YOU AGAIN SOON!")
print("---------------------")



