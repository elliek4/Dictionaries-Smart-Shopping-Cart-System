# Ellie Khoo
# AM

# dictionary for products, keys are the product, values are the prices
products = {
    "Milk": 4.99,
    "Yogurt": 3.49,
    "Chocolate Bar": 2.99,
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

    new_quantity = shopping_cart[list(shopping_cart)[removed_item - 1]] - 1

    print(f"Removed 1 {list(shopping_cart)[removed_item - 1]} from your cart!")
    print(f"{list(shopping_cart)[removed_item - 1]} quantity is now {new_quantity}")




while user_choice != 6:

    if user_choice == 1:
        display_products(products)
    elif user_choice == 2:
        add_product(products, shopping_cart)
    elif user_choice == 3:
        remove_product(shopping_cart)
        

    user_choice = main_menu()