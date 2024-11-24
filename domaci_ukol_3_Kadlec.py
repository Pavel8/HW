class Airplane:
    def __init__(self, airplane_type, max_passengers):
        # Inicializace letadla s typem a maximálním počtem pasažérů
        self.airplane_type = airplane_type  # Typ letadla (např. "Boeing 747")
        self.max_passengers = max_passengers  # Maximální počet pasažérů, které může letadlo přepravit
        self.current_passengers = 0  # Aktuální počet pasažérů v letadle (zpočátku 0)

    def __str__(self):
        # Zobrazí informace o letadle ve formátu: Typ letadla, aktuální pasažéři, maximální kapacita
        return f"Airplane Type: {self.airplane_type}, Current Passengers: {self.current_passengers}, Max Passengers: {self.max_passengers}"

    # Přetížení operátoru pro rovnost (==)
    def __eq__(self, other):
        if not isinstance(other, Airplane):  # Pokud se nejedná o jiný objekt typu Airplane
            return False
        # Porovnání typu letadla (pokud je stejný typ letadla, vrátí True)
        return self.airplane_type == other.airplane_type

    # Přetížení operátoru pro sčítání (+) - zvyšování počtu pasažérů
    def __add__(self, number):
        if number < 0:
            # Pokud se pokusíme přidat záporný počet pasažérů, vyvolá to chybu
            raise ValueError("Cannot increase passengers by a negative number")
        # Spočítá nový počet pasažérů po přidání
        new_passenger_count = self.current_passengers + number
        if new_passenger_count > self.max_passengers:
            # Pokud je nový počet pasažérů větší než maximální kapacita, vyvolá to chybu
            raise ValueError("Cannot add more passengers than the maximum capacity")
        # Nastaví nový počet pasažérů
        self.current_passengers = new_passenger_count
        return self

    # Přetížení operátoru pro odečítání (-) - snižování počtu pasažérů
    def __sub__(self, number):
        if number < 0:
            # Pokud se pokusíme odečíst záporný počet pasažérů, vyvolá to chybu
            raise ValueError("Cannot decrease passengers by a negative number")
        # Spočítá nový počet pasažérů po odečtení
        new_passenger_count = self.current_passengers - number
        if new_passenger_count < 0:
            # Pokud by nový počet pasažérů byl menší než 0, vyvolá to chybu
            raise ValueError("Cannot have a negative number of passengers")
        # Nastaví nový počet pasažérů
        self.current_passengers = new_passenger_count
        return self

    # Přetížení operátoru pro sčítání přiřazením (+=)
    def __iadd__(self, number):
        # Používá se pro in-place přičítání, stejně jako u operátoru +
        return self.__add__(number)

    # Přetížení operátoru pro odečítání přiřazením (-=)
    def __isub__(self, number):
        # Používá se pro in-place odečítání, stejně jako u operátoru -
        return self.__sub__(number)

    # Přetížení operátoru větší než (>)
    def __gt__(self, other):
        if not isinstance(other, Airplane):  # Pokud se nejedná o letadlo
            raise ValueError("Cannot compare with non-Airplane object")
        # Porovnání maximální kapacity letadel
        return self.max_passengers > other.max_passengers

    # Přetížení operátoru menší než (<)
    def __lt__(self, other):
        if not isinstance(other, Airplane):  # Pokud se nejedná o letadlo
            raise ValueError("Cannot compare with non-Airplane object")
        # Porovnání maximální kapacity letadel
        return self.max_passengers < other.max_passengers

    # Přetížení operátoru větší nebo rovno (>=)
    def __ge__(self, other):
        if not isinstance(other, Airplane):  # Pokud se nejedná o letadlo
            raise ValueError("Cannot compare with non-Airplane object")
        # Porovnání maximální kapacity letadel
        return self.max_passengers >= other.max_passengers

    # Přetížení operátoru menší nebo rovno (<=)
    def __le__(self, other):
        if not isinstance(other, Airplane):  # Pokud se nejedná o letadlo
            raise ValueError("Cannot compare with non-Airplane object")
        # Porovnání maximální kapacity letadel
        return self.max_passengers <= other.max_passengers


# Příklad použití:

# Vytvoření dvou instancí letadel
airplane1 = Airplane("Boeing 747", 400)
airplane2 = Airplane("Airbus A380", 500)

# Testování operátoru rovnosti (==)
print(airplane1 == airplane2)  # Mělo by to vrátit False (různé typy letadel)

# Testování přidání pasažérů pomocí operátoru +
airplane1 + 50  # Přidáme 50 pasažérů
print(airplane1)  # Mělo by to vytisknout: Airplane Type: Boeing 747, Current Passengers: 50, Max Passengers: 400

# Testování odečítání pasažérů pomocí operátoru -
airplane1 - 20  # Odebereme 20 pasažérů
print(airplane1)  # Mělo by to vytisknout: Airplane Type: Boeing 747, Current Passengers: 30, Max Passengers: 400

# Testování přičítání přiřazením (+=) a odečítání přiřazením (-=)
airplane1 += 100  # Přidáme 100 pasažérů
print(airplane1)  # Mělo by to vytisknout: Airplane Type: Boeing 747, Current Passengers: 130, Max Passengers: 400

airplane1 -= 30  # Odebereme 30 pasažérů
print(airplane1)  # Mělo by to vytisknout: Airplane Type: Boeing 747, Current Passengers: 100, Max Passengers: 400

# Testování porovnání na základě maximální kapacity pasažérů
print(airplane1 > airplane2)  # Mělo by to vrátit False (kapacita airplane1 je 400, airplane2 je 500)
print(airplane1 < airplane2)  # Mělo by to vrátit True
print(airplane1 >= airplane2)  # Mělo by to vrátit False
print(airplane1 <= airplane2)  # Mělo by to vrátit True
Vysvětlení: