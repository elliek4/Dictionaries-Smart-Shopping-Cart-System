# Ellie Khoo
# AM

# imported date time module
from datetime import date
current_date = date.today()
# dictionary for products, keys are the product, values are the prices
products = {
    "Carrot": 0.30,
    "Yogurt": 3.49,
    "Garlic": 0.75,
    "Cereal": 4.99,
    "Cheese": 3.99
    }

# create empty dictionary to store products and how many that the user wants to buy
shopping_cart = {}

# created function for main menu that displays system options to user
# function also validates user's choice that it is in range, otherwise continues asking 
# returns user's choice to use as condition of loop of showing menu until user exits
def main_menu():
    print()
    print("================ SMART SHOPPING CART ===============")
    print()
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")

    print()
    user_choice = int(input("Enter your choice: "))
    
    while user_choice < 1 or user_choice > 6:
        print("Invalid option!")
        user_choice = int(input("Enter your choice: "))
        print()
    
    return user_choice

# calls menu function to get user's first option
user_choice = main_menu()

# function to display all available products 
# uses loop through dictionary to show items and prices
def display_products(products):
    print()
    for index, (item, price) in enumerate(products.items()):
        print(f"{index + 1}. {item}    ${price:.2f}")
        
# function to add products and quantities that users want to buy
# displays products using for loop to go through dictionary
def add_product(products, shopping_cart):
    print()
    for index, (item) in enumerate(products):
        print(f"{index + 1}. {item}")
    
    print()
    add_product = int(input("Enter product number: "))

    while add_product < 1 or add_product > len(products):
        print("Invalid product number!")
        add_product = int(input("Enter product number: "))
        print()
    
    # asks for quantity user wants to add
    quantity_added = int(input(f"How many {list(products)[add_product - 1]} do you want? "))
    
    # checks whether user has valid answer, otherwise asks again
    while quantity_added < 0:
        print("Invalid quantity!")
        quantity_added = int(input(f"How many {list(products)[add_product - 1]} do you want? "))
        print()
    
    # keeps track of quantity user adds of specific product
    # quantity added is displayed as total quantity if its the first time user added the product to the cart
    # otherwise adds quantity added to quantity stored in dictionary to display total quantity
    total_quantity = 0
    if list(products)[add_product - 1] not in shopping_cart:
        shopping_cart[list(products)[add_product - 1]] = quantity_added
        total_quantity = quantity_added
    else:
        total_quantity = shopping_cart[list(products)[add_product - 1]] + quantity_added
        shopping_cart[list(products)[add_product - 1]] = total_quantity

    # prints information to user how much of the product they added and how much they currently have
    print(f"Added {quantity_added} {list(products)[add_product - 1]} to your cart!")
    print(f"{list(products)[add_product - 1]} quantity is now {total_quantity}.")
    print()

# function for the user to remove products
# first displays shopping cart using loop, enumerate, and dictionary
# asks what user wants to remove and how many, then removes it
def remove_product(shopping_cart):
    print() 

    # checks if shopping cart is empty, ends function if it is
    if len(shopping_cart) == 0:
        print("There is nothing in your shopping cart!")
        return 

    print("=============== YOUR SHOPPING CART ===============")
    print()

    for index, (item, quantity) in enumerate(shopping_cart.items()):
        print(f"{index + 1}. {item} - Quantity: {quantity}")
    print()

    # asks user which item they want to remove
    removed_item = int(input("Enter item number to remove: "))

    # uses loop to repeat until user chooses valid item number
    while removed_item < 1 or removed_item > len(shopping_cart):
        print("Invalid item!")
        removed_item = int(input("Enter item number to remove: "))
        print()

    # gets new quantity by subtracting one from the old quantity
    new_quantity = shopping_cart[list(shopping_cart)[removed_item - 1]] - 1
    
    # makes sure quantity doesn't become negative
    if new_quantity < 0:
        new_quantity = 0
    
    # make the product have the new quantity in the dictionary
    shopping_cart[list(shopping_cart)[removed_item - 1]] = new_quantity

    # prints how many of the product are now in the cart
    print(f"Removed 1 {list(shopping_cart)[removed_item - 1]} from your cart!")
    print(f"{list(shopping_cart)[removed_item - 1]} quantity is now {new_quantity}")

    if new_quantity == 0:
        del shopping_cart[list(shopping_cart)[removed_item - 1]]

# function to show user the products, quantity, and price in their shopping cart
def display_cart(shopping_cart, products):
    print()

    # checks if shopping cart is empty, ends function if it is
    if len(shopping_cart) == 0:
        print("There is nothing in your shopping cart!")
        return 
    
    # variables to keep track of total items and subtotal
    total_items = 0
    subtotal = 0

    # uses for loop with enumerate and dictionary to print numbered list, 
    # unit price, quantity, and total of each product 
    print("=============== YOUR SHOPPING CART ===============")
    print()
    print(f"Product     Unit Price     Quantity     Line Total")
    for index, (product, quantity) in enumerate(shopping_cart.items()):
        print(f"{index+1}. {product}      ${(products[product]):.2f}          {quantity}          ${(products[product] * quantity):.2f}")
        
        total_items += quantity
        subtotal += (products[product] * quantity)
    print()

    # prints total items and subtotal using variables that kept track in loop
    print(f"Total items: {total_items}")
    print(f"Subtotal: ${subtotal:.2f}")

    # return subtotal so it can be used in calculate current total function
    return subtotal

# function to calculate subtotal by multiplying quantity of each product by its price
def calculate_total(shopping_cart, products):
    print()
    print("=============== CURRENT TOTAL ===============")
    subtotal = 0
    for product, quantity in shopping_cart.items():
        subtotal += (quantity * products[product])
    print()
    
    # prints subtotal rounded to 2 decimals
    print(f"Subtotal: ${subtotal:.2f}")

    # returns subtotal to be used to calculate discounts and checkout
    return subtotal


# loops through options and calls functions depending on user's choice
# always loops back to menu function after 
# if option 6 is chosen, loop is exited
while user_choice != 6 or len(shopping_cart) == 0:

    if user_choice == 1:
        display_products(products)
    elif user_choice == 2:
        add_product(products, shopping_cart)
    elif user_choice == 3:
        remove_product(shopping_cart)
    elif user_choice == 4:
        display_cart(shopping_cart, products)
    elif user_choice == 5:
        calculate_total(shopping_cart, products)
    elif user_choice == 6:
        print()
        print("You cannot checkout!")
        print("Please fill your shopping cart.")

    user_choice = main_menu()

# gets subtotal from function
subtotal = calculate_total(shopping_cart, products)

# function to calculate discount after user chooses checkout
#  exits loop and evaluates discount based on subtotal
def calculate_discount(subtotal):
    discount = 0
    if subtotal > 40:
        discount = 0.15
    elif subtotal >= 20:
        discount = 0.1
    elif subtotal >= 10:
        discount = 0.05

    return discount

# gets amount saved by multiplying discount by subtotal
amount_saved = subtotal * calculate_discount(subtotal)

#  gets final total by multiplying subtotal by discounted 
# amount and subtracting that from subtotal
final_total = subtotal - amount_saved


# prints final receipt including shopping cart, discount, amount saved, and final total
print()
print("=============== RECEIPT ===============")
print(current_date)
print()
if subtotal > 0:
    print(f"Product     Unit Price     Quantity     Line Total")
    for index, (product, quantity) in enumerate(shopping_cart.items()):
        print(f"{index+1}. {product}      ${(products[product]):.2f}          {quantity}          ${(products[product] * quantity):.2f}")
print()
print(f"Discount: {calculate_discount(subtotal) * 100}%")
print(f"Amount Saved: ${amount_saved:.2f}")
print(f"Final Total: ${final_total:.2f}")
print()
print("Thank you for shopping!")
print()

