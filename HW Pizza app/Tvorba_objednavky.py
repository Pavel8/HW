from Order_Sales import Order

# Globální seznamy pro pizzy a toppingy
pizza_menu = []
topping_menu = []

def create_order():
    order = Order()
    print("\n--- Vytvoření objednávky ---")
    print("Dostupné pizzy:")

    for i, pizza in enumerate(pizza_menu):
        print(f"{i + 1}. {pizza}")

    pizza_choice = int(input("Vyberte pizzu (číslo): ")) - 1
    selected_pizza = pizza_menu[pizza_choice]
    size_choice = input("Vyberte velikost (Medium / Large): ").capitalize()

    while True:
        add_topping = input("Chcete přidat topping? (Ano/Ne): ").lower()
        if add_topping == "ano":
            print("Dostupné toppingy:")
            for i, topping in enumerate(topping_menu):
                print(f"{i + 1}. {topping.name} (Medium: {topping.price_medium}€, Large: {topping.price_large}€)")
            topping_choice = int(input("Vyberte topping (číslo): ")) - 1
            selected_topping = topping_menu[topping_choice]
            selected_pizza.add_topping(selected_topping, size_choice)
        elif add_topping == "ne":
            break
        else:
            print("Neplatná volba.")

    order.add_pizza(selected_pizza, size_choice)
    print(f"Objednávka vytvořena:\n{order}")
    print(f"Celková cena: {order.calculate_total()}€")

    # Zjištění, zda chce zákazník další pizzu
    another_pizza = input("Chcete přidat další pizzu? (Ano/Ne): ").lower()
    if another_pizza == 'ano':
        create_order()
    else:
        print(f"Celková částka k úhradě: {order.calculate_total()}€")
