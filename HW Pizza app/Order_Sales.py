from Pizza_classes import Pizza

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