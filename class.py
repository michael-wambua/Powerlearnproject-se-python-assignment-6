# Main Class
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # Battery life in hours

    def make_call(self, number):
        print(f"Calling {number} from {self.model}... 📞")

    def charge_battery(self):
        print(f"Charging {self.model}... 🔋")

# Child Class - Gaming Phone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, cooling_system):
        super().__init__(brand, model, battery_life)
        self.cooling_system = cooling_system  # Additional attribute

    def enable_gaming_mode(self):
        print(f"Gaming mode ON for {self.model}! 🎮")

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S21", 20)
gaming_phone = GamingPhone("Asus", "ROG Phone 6", 30, "Advanced Liquid Cooling")

# Using methods
phone1.make_call("123456789")
phone1.charge_battery()
gaming_phone.enable_gaming_mode()
