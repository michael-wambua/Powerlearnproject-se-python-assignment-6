from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

# Car class
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

# Plane class
class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

# Boat class
class Boat(Vehicle):
    def move(self):
        print("Sailing on water 🚢")

# Creating objects
vehicles = [Car(), Plane(), Boat()]

# Demonstrating polymorphism
for v in vehicles:
    v.move()
