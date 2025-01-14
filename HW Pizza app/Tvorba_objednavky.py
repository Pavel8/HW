from Order_Sales import Order
from Data_Pizza import load_pizza_menu
from Data_Pizza import pizza_menu
from Data_Pizza import topping_menu
from Objednavky_funkce import *


def create_order():
    total_price = 0  # Zde budeme uchovávat celkovou cenu objednávky
    order = Order()
    print("\n--- Vytvoření objednávky ---")

    while True:
        print("Dostupné pizzy:")
        for i, pizza in enumerate(pizza_menu):
            print(f"{i + 1}. {pizza}")

        pizza_choice = int(input("Vyberte pizzu (číslo): ")) - 1
        selected_pizza = pizza_menu[pizza_choice]

        while True:
            size_choice = input("Vyberte velikost (Medium / Large): ").capitalize()
            if size_choice in ["Medium", "Large"]:
                break
            else:
                print("Neplatná volba. Zadejte 'Medium' nebo 'Large'.")

        while True:
            add_topping = input("Chcete přidat topping? (Ano/Ne): ").lower()
            if add_topping == "ano":
                print("Dostupné toppingy:")
                for i, topping in enumerate(topping_menu):
                    print(f"{i + 1}. {topping.name} ({topping.price}€)")
                topping_choice = int(input("Vyberte topping (číslo): ")) - 1
                selected_topping = topping_menu[topping_choice]
                selected_pizza.add_topping(selected_topping)
            elif add_topping == "ne":
                break
            else:
                print("Neplatná volba.")

        order.add_pizza(selected_pizza, size_choice)
        pizza_price = selected_pizza.calculate_price(size_choice)
        total_price += pizza_price
        print(f"Pizza přidána do objednávky. Cena: {pizza_price}€")
        print(f"Aktuální celková cena: {total_price}€")

        another_pizza = input("Chcete přidat další pizzu? (Ano/Ne): ").lower()
        if another_pizza != "ano":
            break

    print(f"Celková částka k úhradě: {total_price}€")
    save_order(order)  # Uložení objednávky do databáze
    print("Objednávka byla uložena.")