import math

class Tvar: 
    def obsah(self):
#        """This method should be overridden by subclasses."""
        raise NotImplementedError("Podtřídy musí implementovat metodu 'obsah'.")


class Obdelnik(Tvar):
    def __init__(self, sirka, vyska):
        self.sirka = sirka
        self.vyska = vyska

    def obsah(self):
        return self.sirka * self.vyska


class Kruh(Tvar): 
    def __init__(self, polomer):
        self.polomer = polomer

    def obsah(self):
        return math.pi * (self.polomer ** 2)


class PravyTrojuhelnik(Tvar): 
    def __init__(self, zakladna, vyska):
        self.zakladna = zakladna
        self.vyska = vyska

    def obsah(self):
        return 0.5 * self.zakladna * self.vyska


class Lichobeznik(Tvar):  
    def __init__(self, zakladna1, zakladna2, vyska):
        self.zakladna1 = zakladna1
        self.zakladna2 = zakladna2
        self.vyska = vyska

    def obsah(self):
        return 0.5 * (self.zakladna1 + self.zakladna2) * self.vyska
    
obdelnik = Obdelnik(3, 10)
kruh = Kruh(3)
pravy_trojuhelnik = PravyTrojuhelnik(3, 8)
lichobeznik = Lichobeznik(4, 2, 5)

# Print areas of each shape
print(f"Obdélník: {obdelnik.obsah()}") 
print(f"Kruh: {kruh.obsah()}") 
print(f"Pravý trojúhelník: {pravy_trojuhelnik.obsah()}") 
print(f"Lichoběžník: {lichobeznik.obsah()}") 