import json
from Pizza_classes import *

# Globální seznamy pro pizzy a toppingy
pizza_menu = []
topping_menu = []


# Funkce pro načítání pizz ze souboru
def load_pizza_menu():
    try:
        # Načteme data ze souboru pizza_data.json
        with open("pizza_data.json", "r") as file:
            pizza_data = json.load(file)

        # Obnovíme seznam pizz z načtených dat
        for pizza_info in pizza_data:
            pizza = Pizza(pizza_info["name"])
            pizza.set_price(pizza_info["sizes"]["Medium"], pizza_info["sizes"]["Large"])
            pizza_menu.append(pizza)
        print("Pizzy byly úspěšně načteny.")

    except FileNotFoundError:
        # Pokud soubor neexistuje, vypíšeme informaci a pokračujeme bez načítání
        print("Soubor s pizzami nenalezen, začínáme s prázdným seznamem pizz.")


# Funkce pro ukládání pizz do souboru
def save_pizza_menu():
    # Vytvoření seznamu pro uložení do souboru
    pizza_data = [{"name": pizza.name, "sizes": pizza.sizes} for pizza in pizza_menu]

    # Uložení seznamu pizz do souboru pizza_data.json
    with open("pizza_data.json", "w") as file:
        json.dump(pizza_data, file, indent=4)
    print("Pizzy byly úspěšně uloženy.")