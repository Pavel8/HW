class Airplane:
    def __init__(self, airplane_type, max_passengers):
        self.airplane_type = airplane_type  
        self.max_passengers = max_passengers 
        self.current_passengers = 0 

    def __str__(self):
        return f"Airplane Type: {self.airplane_type}, Current Passengers: {self.current_passengers}, Max Passengers: {self.max_passengers}"

    # Přetížení operátoru pro rovnost (==)
    def __eq__(self, other):
        if type(other) is not Airplane:  # Pokud neni letadlo
            return False
        else:    # Porovnání typu letadla
            return self.airplane_type == other.airplane_type

    def __add__(self, number):
        if number < 0:
            raise ValueError
        new_passenger_count = self.current_passengers + number
        if new_passenger_count > self.max_passengers:
            raise ValueError("Překročili jste maximální kapacitu letadla")
        self.current_passengers = new_passenger_count
        return self

    def __sub__(self, number):
        if number < 0:
            raise ValueError("Nemuzeme odecitat zaporny pocet")
        # Spočítá nový počet pasažérů po odečtení
        new_passenger_count = self.current_passengers - number
        if new_passenger_count < 0:
            raise ValueError("Nejde mit mene nez 0 pasazeru")
        # Nastaví nový počet pasažérů
        self.current_passengers = new_passenger_count
        return self


    def __gt__(self, other):
        if not isinstance(other, Airplane): 
            raise ValueError
        # Porovnání maximální kapacity letadel
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        if not isinstance(other, Airplane):
            raise ValueError
        # Porovnání maximální kapacity letadel
        return self.max_passengers < other.max_passengers

    # Přetížení operátoru větší nebo rovno (>=)
    def __ge__(self, other):
        if not isinstance(other, Airplane):
            raise ValueError
        # Porovnání maximální kapacity letadel
        return self.max_passengers >= other.max_passengers

    # Přetížení operátoru menší nebo rovno (<=)
    def __le__(self, other):
        if not isinstance(other, Airplane):
            raise ValueError
        # Porovnání maximální kapacity letadel
        return self.max_passengers <= other.max_passengers


# Příklad použití:

# Vytvoření dvou letadel
airplane1 = Airplane("Boeing 747", 400)
airplane2 = Airplane("Airbus A380", 500)

print(airplane1 == airplane2) 

# Testování přidání pasažérů
airplane1 + 50 
print(airplane1) 

# Testování odečítání pasažérů
airplane1 - 20 
print(airplane1) 

print(airplane1 > airplane2)  
print(airplane1 < airplane2)  
print(airplane1 >= airplane2) 
print(airplane1 <= airplane2)