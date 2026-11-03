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

user_choice = main_menu()

def view_available_products(products):
    print()
    for index, (item, price) in enumerate(products.items()):
        print(f"{index + 1}. {item}    ${price:.2f}")
        

def add_products_and_quantities(products):
    print()
    for index, (item) in enumerate(products):
        print(f"{index + 1}. {item}")



while user_choice != 6:

    if user_choice == 1:
        view_available_products(products)
    elif user_choice == 2:
        add_products_and_quantities(products)



    user_choice = main_menu()