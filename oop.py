# Activity 1: Design Your Own Class! 🏗️
class Smartphone:
    def __init__(self, brand, model, price, battery_percentage):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery_percentage = battery_percentage

    def charge(self):
        self.battery_percentage = 100
        print(f"{self.model} is now fully charged!")

    def use_app(self, app_name):
        if self.battery_percentage > 0:
            self.battery_percentage -= 10
            print(f"Using {app_name}. Battery is now at {self.battery_percentage}%")
        else:
            print("Battery is dead! Please charge your phone.")

    def display_info(self):
        print(f"Smartphone Info: {self.brand} {self.model}, ${self.price}, Battery: {self.battery_percentage}%")

class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, battery_percentage, heart_rate_monitor):
        super().__init__(brand, model, price, battery_percentage)
        self.heart_rate_monitor = heart_rate_monitor

    def fitness_tracking(self):
        print(f"Tracking fitness activity with {self.model}'s heart rate monitor.")
    
    def display_info(self):
        super().display_info()
        print(f"Heart Rate Monitor: {self.heart_rate_monitor}")

# Activity 2: Polymorphism Challenge! 🎭
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Creating objects of Smartphone and Smartwatch
phone = Smartphone("Samsung", "Galaxy S21", 799, 50)
watch = Smartwatch("Apple", "Watch Series 6", 399, 80, True)

# Using methods for Smartphone and Smartwatch
phone.display_info()
phone.use_app("Instagram")
phone.charge()

watch.display_info()
watch.fitness_tracking()

# Creating objects of Vehicle, Car, Plane, and Boat
vehicles = [Car(), Plane(), Boat()]

# Polymorphism: Calling move() on different vehicle objects
for vehicle in vehicles:
    vehicle.move()  # Each vehicle has a different behavior for move()
