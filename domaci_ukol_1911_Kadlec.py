class Device:
    def __init__(self, znacka, model):
        self.znacka = znacka
        self.model = model

    def ukaz_info(self):
        """Displays basic device information."""
        return f"Device: {self.znacka} {self.model}"

    def zapnout(self):
        return f"{self.model} je zapnuty."

    def vypnout(self):
        """Turns off the device."""
        return f"{self.model} je vypnuty."


class CoffeeMachine(Device):
    def __init__(self, znacka, model, kapacita_vody):
        super().__init__(znacka, model)
        self.kapacita_vody = kapacita_vody

    def brew_coffee(self):
        return f"Priprava kavy o {self.kapacita_vody}l vody."

# Subclass for Blender
class Blender(Device):
    def __init__(self, znacka, model, speed_levels, has_ice_crush_function):
        super().__init__(znacka, model)
        self.speed_levels = speed_levels  # number of speed settings
        self.has_ice_crush_function = has_ice_crush_function  # boolean

    def blend(self):
        """Simulates blending action."""
        return f"Blending at {self.speed_levels} speed settings."

    def display_info(self):
        """Override to include blender specific information."""
        ice_crush_info = "with ice crush" if self.has_ice_crush_function else "without ice crush"
        return f"Blender: {self.znacka} {self.model}, Speed Levels: {self.speed_levels}, {ice_crush_info}"


# Subclass for MeatGrinder
class MeatGrinder(Device):
    def __init__(self, znacka, model, grind_capacity, is_electric):
        super().__init__(znacka, model)
        self.grind_capacity = grind_capacity  # in kg per minute
        self.is_electric = is_electric  # boolean indicating if it's electric or manual

    def grind_meat(self):
        """Simulates the grinding process."""
        return f"Grinding meat at {self.grind_capacity} kg per minute."

    def display_info(self):
        """Override to include meat grinder specific information."""
        power_type = "electric" if self.is_electric else "manual"
        return f"Meat Grinder: {self.znacka} {self.model}, Grind Capacity: {self.grind_capacity}kg/min, Type: {power_type}"


# Example usage
coffee_machine = CoffeeMachine("Keurig", "K-Supreme", 1500, 1.8, True)
blender = Blender("Ninja", "BL770", 1500, 3, True)
meat_grinder = MeatGrinder("KitchenAid", "KG25", 350, 2, True)

# Display information
print(coffee_machine.display_info())
print(blender.display_info())
print(meat_grinder.display_info())

# Using methods
print(coffee_machine.brew_coffee())
print(blender.blend())
print(meat_grinder.grind_meat())

# Turning devices on and off
print(coffee_machine.turn_on())
print(blender.turn_off())
print(meat_grinder.turn_on())