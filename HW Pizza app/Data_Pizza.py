import csv
import os
from Pizza_classes import Pizza, Topping



# Výchozí seznam pizz
pizza_menu = [
    Pizza("Margherita", 5.0,  7.0),
    Pizza("Pepperoni", 6.0,  8.0),
    Pizza("Vegetarian", 5.0,  7.0),
    Pizza("Hawaiian", 5.0,  7.0),

]

# Výchozí seznam toppingů
topping_menu = [
    Topping("Olives", 1.0),
    Topping("Mushrooms", 1.2),
    Topping("Pepperoni", 1.5),
    Topping("Onions", 0.8),
    Topping("Ham", 1.5),
    Topping("Pineapple", 1.3),
    Topping("Bacon", 1.7),
    Topping("Extra Cheese", 1.4),
    Topping("Green Peppers", 1.0),
    Topping("Tomatoes", 0.9)
]

# Funkce pro uložení menu do CSV souboru
# Funkce pro uložení menu do CSV souboru
def save_pizza_menu():
    try:
        with open("Pizza_databaze.csv", "w", newline="") as file:
            writer = csv.writer(file)
            # Zápis hlavičky
            writer.writerow(["Name", "MediumPrice", "LargePrice"])
            # Zápis dat
            for pizza in pizza_menu:
                if isinstance(pizza.sizes, dict) and "Medium" in pizza.sizes and "Large" in pizza.sizes:
                    if isinstance(pizza.sizes["Medium"], (int, float)) and isinstance(pizza.sizes["Large"], (int, float)):
                        writer.writerow([pizza.name, pizza.sizes["Medium"], pizza.sizes["Large"]])
                    else:
                        print(f"Chybný formát cen u pizzy: {pizza.name}")
                else:
                    print(f"Chybné nebo neúplné informace o velikostech u pizzy: {pizza}")
        print("Pizzy byly úspěšně uloženy do Pizza_databaze.csv.")
    except Exception as e:
        print(f"Chyba při ukládání pizz: {e}")




def load_pizza_menu():
    try:
        if not os.path.exists("Pizza_databaze.csv") or os.path.getsize("Pizza_databaze.csv") == 0:
            print("Soubor Pizza_databaze.csv neexistuje nebo je prázdný. Ukládám výchozí pizzy.")
            save_pizza_menu()
        else:
            with open("Pizza_databaze.csv", "r") as file:
                reader = csv.reader(file)
                next(reader)  # Přeskočení hlavičky
                for row in reader:
                    name, medium_price, large_price = row
                    pizza_menu.append(Pizza(name, {"Medium": float(medium_price)}, {"Large": float(large_price)}))
            print("Pizzy byly úspěšně načteny z Pizza_databaze.csv.")
    except Exception as e:
        print(f"Chyba při načítání pizz: {e}")

def save_topping_menu():
    try:
        with open("Topping_databaze.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Price"])
            for topping in topping_menu:
                writer.writerow([topping.name, topping.price])
        print("Toppingy byly úspěšně uloženy do Topping_databaze.csv.")
    except Exception as e:
        print(f"Chyba při ukládání toppingů: {e}")

def load_topping_menu():
    try:
        if not os.path.exists("Topping_databaze.csv") or os.path.getsize("Topping_databaze.csv") == 0:
            print("Soubor Topping_databaze.csv neexistuje nebo je prázdný. Ukládám výchozí toppingy.")
            topping_menu.extend(topping_menu)
            save_topping_menu()
        else:
            with open("Topping_databaze.csv", "r") as file:
                reader = csv.reader(file)
                next(reader)  # Přeskočení hlavičky
                for row in reader:
                    name, price = row
                    topping_menu.append(Topping(name, float(price)))
            print("Toppingy byly úspěšně načteny z Topping_databaze.csv.")
    except Exception as e:
        print(f"Chyba při načítání toppingů: {e}")
