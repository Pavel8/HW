import json
from Pizza_classes import *


def save_data():
    pizza_data = [{
        "name": pizza.name,
        "sizes": pizza.sizes
    } for pizza in pizza_menu]

    topping_data = [{
        "name": topping.name,
        "price_medium": topping.price_medium,
        "price_large": topping.price_large
    } for topping in topping_menu]

    with open('pizza_data.json', 'w') as pizza_file:
        json.dump(pizza_data, pizza_file, indent=4)

    with open('topping_data.json', 'w') as topping_file:
        json.dump(topping_data, topping_file, indent=4)
    print("Data byla úspěšně uložena.")


def load_data():
    global pizza_menu, topping_menu

    try:
        with open('pizza_data.json', 'r') as pizza_file:
            pizza_data = json.load(pizza_file)
            pizza_menu = [Pizza(pizza['name'], pizza['sizes']['Medium'], pizza['sizes']['Large']) for pizza in
                          pizza_data]

        with open('topping_data.json', 'r') as topping_file:
            topping_data = json.load(topping_file)
            topping_menu = [Topping(topping['name'], topping['price_medium'], topping['price_large']) for topping in
                            topping_data]

        print("Data byla úspěšně načtena.")

    except FileNotFoundError:
        print("Soubor neexistuje. Začínáme s prázdným seznamem.")
