from Pizza_classes import *
from Order_Sales import *
from Data_Pizza import save_pizza_menu
from Order_Sales import Sales


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
        print(Sales.get_sales_report())
    elif choice == '4':
        display_pizza_menu()
    elif choice == '5':
        display_topping_menu()
    elif choice == '6':
        pass
    else:
        print("Neplatná volba.")


#funkce na zadavani ceny
def get_float_input(prompt: str) -> float:
    while True:
        try:
            # Přečteme vstup od uživatele
            user_input = input(prompt)

            # Nahradíme čárku tečkou
            user_input = user_input.replace(",", ".")

            # Pokusíme se převést na float
            value = float(user_input)

            # Zkontrolujeme, zda je hodnota kladná
            if value < 0:
                print("Cena musí být kladná.")
            else:
                return value  # Pokud je vstup validní, vrátíme hodnotu

        except ValueError:  # Pokud nastane chyba při převodu na float
            print("Neplatný vstup, zadejte číselnou hodnotu.")


def add_pizza():
    pizza_name = input("Zadejte název pizzy: ")
    try:
        medium_price = float(input("Zadejte cenu pro Medium: "))
        large_price = float(input("Zadejte cenu pro Large: "))
    except ValueError:
        print("Neplatný vstup. Cena musí být číslo.")
        return

    # Vytvoření nové instance pizzy s předanými argumenty
    new_pizza = Pizza(pizza_name, medium_price, large_price)
    pizza_menu.append(new_pizza)
    print(f"Pizzu {pizza_name} byla úspěšně přidána.")

    # Ladicí výpis
    print("Aktuální seznam pizz:", pizza_menu)

    # Uložení aktualizovaného seznamu pizz
    save_pizza_menu(pizza_menu)




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

