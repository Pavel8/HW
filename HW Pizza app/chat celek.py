# Topping třída
class Topping:
    def __init__(self, name: str, price_medium: float, price_large: float):
        self.name = name
        self.price_medium = price_medium
        self.price_large = price_large

    def __str__(self):
        return f"{self.name} (+{self.price_medium}€ / {self.price_large}€)"


# Pizza třída
class Pizza:
    def __init__(self, name: str):
        self.name = name
        self.sizes = {"Medium": None, "Large": None}  # Prices for each size
        self.toppings = []

    def set_price(self, medium_price: float, large_price: float):
        self.sizes["Medium"] = medium_price
        self.sizes["Large"] = large_price

    def add_topping(self, topping: Topping, size: str):
        self.toppings.append((topping, size))

    def calculate_price(self, size: str):
        total_price = self.sizes[size]
        for topping, topping_size in self.toppings:
            if topping_size == size:
                total_price += topping.price_medium if size == "Medium" else topping.price_large
        return total_price

    def __str__(self):
        toppings_str = ', '.join(str(topping) for topping, _ in self.toppings)
        return f"{self.name} - {toppings_str}"


# Order třída
class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza: Pizza, size: str):
        self.pizzas.append((pizza, size))

    def calculate_total(self):
        total_price = 0
        for pizza, size in self.pizzas:
            total_price += pizza.calculate_price(size)
        return total_price

    def __str__(self):
        return '\n'.join(f"{pizza} - {size}" for pizza, size in self.pizzas)


# Sales Singleton pro sledování tržeb
class Sales:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Sales, cls).__new__(cls)
            cls._instance.orders = []
        return cls._instance

    def add_order(self, order: Order):
        self.orders.append(order)

    def get_sales_report(self):
        total_sales = sum(order.calculate_total() for order in self.orders)
        return f"Celkový obrat: {total_sales}€"


# Hlavní menu pro aplikaci
def main_menu():
    while True:
        print("\n--- Pizza Ordering App ---")
        print("1. Vytvořit objednávku")
        print("2. Platba")
        print("3. Admin menu")
        print("4. Ukončit aplikaci")

        choice = input("Vyberte možnost: ")

        if choice == '1':
            create_order()
        elif choice == '2':
            process_payment()
        elif choice == '3':
            admin_menu()
        elif choice == '4':
            print("Ukončuji aplikaci.")
            break
        else:
            print("Neplatná volba, zkuste znovu.")


# Funkce pro vytvoření objednávky
def create_order():
    order = Order()
    print("\n--- Vytvoření objednávky ---")
    print("Dostupné pizzy:")

    for i, pizza in enumerate(pizza_menu):
        print(f"{i + 1}. {pizza.name} (Medium: {pizza.sizes['Medium']}€, Large: {pizza.sizes['Large']}€)")

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


# Funkce pro platbu
def process_payment():
    print("\n--- Platba ---")
    # Předpokládáme, že objednávka byla vytvořena, toto bude později rozšířeno.
    print("Platba je zpracována (tento krok bude později rozšířen).")


# Admin menu pro správu pizzy a toppingů
def admin_menu():
    print("\n--- Admin menu ---")
    print("1. Přidat novou pizzu")
    print("2. Přidat nový topping")
    print("3. Zobrazit statistiky prodeje")
    print("4. Vrátit se do hlavního menu")

    choice = input("Vyberte možnost: ")

    if choice == '1':
        add_pizza()
    elif choice == '2':
        add_topping()
    elif choice == '3':
        print(sales.get_sales_report())
    elif choice == '4':
        pass
    else:
        print("Neplatná volba.")


def add_pizza():
    pizza_name = input("Zadejte název pizzy: ")
    medium_price = float(input("Zadejte cenu pro Medium: "))
    large_price = float(input("Zadejte cenu pro Large: "))

    new_pizza = Pizza(pizza_name)
    new_pizza.set_price(medium_price, large_price)
    pizza_menu.append(new_pizza)
    print(f"Pizzu {pizza_name} byla úspěšně přidána.")


def add_topping():
    topping_name = input("Zadejte název toppingu: ")
    medium_price = float(input("Zadejte cenu pro Medium: "))
    large_price = float(input("Zadejte cenu pro Large: "))

    new_topping = Topping(topping_name, medium_price, large_price)
    topping_menu.append(new_topping)
    print(f"Topping {topping_name} byl úspěšně přidán.")


 