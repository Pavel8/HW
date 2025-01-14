class Pizza:
    def __init__(self, name, medium_price, large_price):
        self.name = name
        self.sizes = {
            'Medium': medium_price,
            'Large': large_price
        }
        self.toppings = []

    def add_topping(self, topping):
        if isinstance(topping, Topping):
            self.toppings.append(topping)
            print(f"Topping {topping.name} byl přidán k pizze {self.name}.")
        else:
            print("Přidávaný objekt není typu Topping.")

    def calculate_price(self, size):
        if size not in self.sizes:
            raise ValueError(f"Neplatná velikost: {size}")
        base_price = self.sizes[size]
        total_topping_price = sum(topping.price for topping in self.toppings)
        return base_price + total_topping_price

    def __repr__(self):
        return f"Pizza(name={self.name}, sizes={self.sizes}, toppings={self.toppings})"


class Topping:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (+{self.price}€)"

    def __repr__(self):
        return self.__str__()

