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
    def __init__(self, name: str, medium_price: float, large_price: float):
        self.name = name
        self.sizes = {"Medium": medium_price, "Large": large_price}

    def __str__(self):
        return f"{self.name} - Medium: {self.sizes['Medium']}€, Large: {self.sizes['Large']}€"