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