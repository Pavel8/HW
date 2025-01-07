# Topping třída
class Topping:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (+{self.price}€)"

# Pizza třída
class Pizza:
    def __init__(self, name: str, size: str, base_price: float):
        self.name = name
        self.size = size
        self.base_price = base_price
        self.toppings = []

    def add_topping(self, topping: Topping):
        self.toppings.append(topping)

    def calculate_price(self):
        total_price = self.base_price
        for topping in self.toppings:
            total_price += topping.price
        return total_price

    def __str__(self):
        toppings_str = ', '.join(str(topping) for topping in self.toppings)
        return f"{self.name} ({self.size}) - Base: {self.base_price}€ | Toppings: {toppings_str}"

# Order třída
class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza: Pizza):
        self.pizzas.append(pizza)

    def calculate_total(self):
        total_price = sum(pizza.calculate_price() for pizza in self.pizzas)
        return total_price

    def __str__(self):
        return '\n'.join(str(pizza) for pizza in self.pizzas)

# Test tříd
if __name__ == "__main__":
    # Vytvoření několika toppingů
    topping1 = Topping("Mozzarella", 1.5)
    topping2 = Topping("Pepperoni", 2.0)

    # Vytvoření pizzy a přidání toppingů
    pizza = Pizza("Margarita", "Large", 5.0)
    pizza.add_topping(topping1)
    pizza.add_topping(topping2)

    # Vytvoření objednávky a přidání pizzy
    order = Order()
    order.add_pizza(pizza)

    # Výpis objednávky a celková cena
    print(order)
    print(f"Total Price: {order.calculate_total()}€")