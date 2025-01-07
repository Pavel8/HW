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
    pizza_name = input("Zadejte název pizzy (např. Margarita): ")
    pizza_size = input("Zadejte velikost pizzy (Small, Medium, Large): ")
    pizza_price = float(input("Zadejte cenu pizzy: "))

    pizza = Pizza(pizza_name, pizza_size, pizza_price)

    while True:
        add_topping = input("Chcete přidat topping? (Ano/Ne): ").lower()
        if add_topping == "ano":
            topping_name = input("Zadejte název toppingu: ")
            topping_price = float(input(f"Zadejte cenu toppingu {topping_name}: "))
            topping = Topping(topping_name, topping_price)
            pizza.add_topping(topping)
        elif add_topping == "ne":
            break
        else:
            print("Neplatná volba.")

    order.add_pizza(pizza)
    print(f"Objednávka vytvořena:\n{order}")
    print(f"Celková cena: {order.calculate_total()}€")


# Funkce pro platbu
def process_payment():
    print("\n--- Platba ---")
    # Předpokládejme, že jsme vytvořili objednávku a máme ji
    # Tento krok může být rozšířen o platbu kartou, hotovostí atd.
    print("Platba je zpracována (tento krok bude později rozšířen).")


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


# Implementace v admin menu
def admin_menu():
    sales = Sales()

    print("\n--- Admin menu ---")
    print("1. Zobrazit statistiky prodeje")
    print("2. Vrátit se do hlavního menu")

    choice = input("Vyberte možnost: ")

    if choice == '1':
        print(sales.get_sales_report())
    elif choice == '2':
        pass
    else:
        print("Neplatná volba.")


# Přidání objednávky do Sales
sales = Sales()
order = Order()
pizza = Pizza("Hawaiian", "Large", 6.0)
pizza.add_topping(Topping("Ananas", 1.2))
order.add_pizza(pizza)
sales.add_order(order)

# Spuštění hlavního menu
if __name__ == "__main__":
    main_menu()
