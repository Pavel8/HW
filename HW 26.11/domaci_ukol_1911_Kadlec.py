class Device:
    def __init__(self, znacka, model):
        self.znacka = znacka
        self.model = model

    def ukaz_info(self):
        """Displays basic device information."""
        return f"Device: {self.znacka} {self.model}"

    def zapnout(self):
        return f"{self.model} od {self.znacka} je zapnuty."

    def vypnout(self):
        """Turns off the device."""
        return f"{self.model} od {self.znacka} je vypnuty."


class CoffeeMachine(Device):
    def __init__(self, znacka, model, kapacita_vody):
        Device.__init__(self,znacka, model)
        self.kapacita_vody = kapacita_vody

    def brew_coffee(self):
        return f"Priprava kavy o {self.kapacita_vody}l vody."

class Blender(Device):
    def __init__(self, znacka, model, pocet_rychlosti):
        Device.__init__(self,znacka, model)
        self.pocet_rychlosti = pocet_rychlosti

    def blend(self):
        """Simulates blending action."""
        return f"Ma {self.pocet_rychlosti} rychlosti mleti."


class MeatGrinder(Device):
    def __init__(self, znacka, model, kapacita):
        Device.__init__(self,znacka, model)
        self.kapacita = kapacita 
    

    def grind_meat(self):
        """Simulates the grinding process."""
        return f"Mele {self.kapacita}kg za minutu."


# Example usage
coffee_machine = CoffeeMachine("Delonghi", "K-400", 1.3)
blender = Blender("LidlMix", "A800", 3)
meat_grinder = MeatGrinder("Megamlynek", "KG2-A", 2)


# Using methods
print(coffee_machine.brew_coffee())
print(blender.blend())
print(meat_grinder.grind_meat())

# Turning devices on and off
print(coffee_machine.zapnout())
print(blender.vypnout())
print(meat_grinder.zapnout())