from Pizza_classes import *
from Order_Sales import *


# Admin menu pro správu pizzy a toppingů
def admin_menu():
    print("\n--- Admin menu ---")
    print("1. Přidat novou pizzu")
    print("2. Přidat nový topping")
    print("3. Zobrazit statistiky prodeje")
    print("4. Vypis nabízených pizz")
    print("5. Vypis nabízených toppingů")
    print("6. Vrátit se do hlavního menu")

    choice = input("Vyberte možnost: ")

    if choice == '1':
        add_pizza()
    elif choice == '2':
        add_topping()
    elif choice == '3':
        print(sales.get_sales_report())
    elif choice == '4':
        display_pizza_menu()
    elif choice == '5':
        display_topping_menu()
    elif choice == '6':
        pass
    else:
        print("Neplatná volba.")

def add_pizza():
    pizza_name = input("Zadejte název pizzy: ")
    medium_price = get_float_input("Zadejte cenu pro Medium: ")
    large_price = get_float_input("Zadejte cenu pro Large: ")

    new_pizza = Pizza(pizza_name, medium_price, large_price)
    pizza_menu.append(new_pizza)
    print(f"Pizzu {pizza_name} byla úspěšně přidána.")

def add_topping():
    topping_name = input("Zadejte název toppingu: ")
    medium_price = float(input("Zadejte cenu pro Medium: "))
    large_price = float(input("Zadejte cenu pro Large: "))

    new_topping = Topping(topping_name, medium_price, large_price)
    topping_menu.append(new_topping)
    print(f"Topping {topping_name} byl úspěšně přidán.")

# Funkce pro zobrazení seznamu pizz
def display_pizza_menu():
    print("\n--- Seznam pizz ---")
    if not pizza_menu:
        print("Žádné pizzy nejsou k dispozici.")
    else:
        for pizza in pizza_menu:
            print(f"{pizza.name} - Medium: {pizza.sizes['Medium']}€, Large: {pizza.sizes['Large']}€")

# Funkce pro zobrazení seznamu toppingů
def display_topping_menu():
    print("\n--- Seznam toppingů ---")
    if not topping_menu:
        print("Žádné toppingy nejsou k dispozici.")
    else:
        for topping in topping_menu:
            print(f"{topping.name} - Medium: {topping.price_medium}€, Large: {topping.price_large}€")



# Seznam pizzy a toppingů
pizza_menu = []
topping_menu = []

# Instance pro správu objednávek a tržeb
sales = Sales()

# Příklad přidání počátečních položek
topping_menu.append(Topping("Mozzarella", 1.0, 1.2))
topping_menu.append(Topping("Salam", 1.5, 1.8))
pizza_menu.append(Pizza("Margarita"))
pizza_menu[0].set_price(5.0, 6.0)
