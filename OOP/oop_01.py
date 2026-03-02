# A class is a blueprint for creating objects in Python.
# It defines attributes (data) and methods (functions) that objects will have.
# Objects are instances created from this blueprint(class), enabling reusable code.

'''
Docstring for oop_01
What is OOP?
Defining a class in Python
Creating and using objects
The _init_ method and instance attributes
A simple real-world example
'''

class Car:
    color = "red"
    def drive(self):
        print(f"The {self.color} car is driving.")

print(id(Car))  # Output: (some unique identifier for the Car class)
my_car = Car()
print(id(my_car))  # Output: (some unique identifier for the my_car instance)
my_car.drive()  # Output: The red car is driving!

class CarWithInit:
    def __init__(self, color):
        self.color = color
        
my_blue_car = CarWithInit("blue")
print(my_blue_car.color)  # Output: blue

class CarWithMethod:
    def __init__(self, color):
        self.color = color
    def drive(self):
        print(f"The {self.color} car is driving!")
        
my_green_car = CarWithMethod("green")
my_green_car.drive()  # Output: The green car is driving!

class CarWithAttributes:
    brand = "Toyota"
    
    def __init__(self, color):
        self.color = color
        self.speed = 0

my_car3 = CarWithAttributes("green")
print(my_car3.brand)  # Output: Toyota
print(my_car3.color)  # Output: green


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} the {self.breed} says Woof!")

my_dog = Dog("Max", "Golden")
my_dog.bark()  # Output: Max the Golden says Woof!