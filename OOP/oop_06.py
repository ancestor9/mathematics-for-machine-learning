# This code explores abstraction in Python using a car theme.
# It demonstrates how Abstract Base Classes enforce a common interface for vehicle class.
# The example includes practical application with a Garage class.
'''
Docstring for oop_06
Abstraction in OOP
- Abstraction is the concept of hiding complex implementation details and showing only the necessary features of an object.
- It allows us to focus on what an object does rather than how it does it, promoting modularity and maintainability in code.
- ABC(Abstract Base Class): "추상 클래스", 다른 클래스들이 공통적으로 가져야 할 특징을 정의하는 '설계도' 역할
- abstractmethod: "추상 메서드"를 표시하는 장식자(Decorator), 이 표시가 붙은 함수는 자식 클래스에서 
  반드시 구체적으로 내용을 채워넣어야 한다는 '강제성'을 부여
'''
from abc import ABC, abstractmethod

# Abstract Vehicle parent class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
# Car child class implementing abstraction
class Car(Vehicle):
    def start_engine(self):
        print("Car engine starting with a roar!")
        
class void_car(Vehicle):
    pass    

# Sportcar child class implementing abstraction
class SportCar(Vehicle):
    def start_engine(self):
        print("SportCar engine starting with a high-pitched scream!")
        
# Garage class to demonstrate abstraction
class Garage:    
    def __init__(self):
        self.vehicles = []
    def add_vehicle(self, vehicle):
        if isinstance(vehicle, Vehicle):
            self.vehicles.append(vehicle)
        else:
            print("Only vehicles can be added to the garage.")        
        
        
        
# Test section to match script demonstration
if __name__ == "__main__":
    # Test Car class
    my_car = Car()
    my_car.start_engine()  # Output: Car engine starting with a roar!
    
    # Test SportCar class
    my_sport_car = SportCar()
    my_sport_car.start_engine()  # Output: SportCar engine starting with a high-pitched scream!
    
    # Test Garage class
    my_garage = Garage()
    my_garage.add_vehicle(my_car)
    my_garage.add_vehicle(my_sport_car)
    my_garage.add_vehicle("Invalid Vehicle")  # Output: Only vehicles can be added to the garage.
    print(my_garage.vehicles)  # Output: [<__main__.Car object at 0x...>, <__main__.SportCar object at 0x...>]
    print("\n--- Garage Vehicles ---")
    for vehicle in my_garage.vehicles:
        vehicle.start_engine()  # Output: Car engine starting with a roar! and SportCar engine starting with a high-pitched scream!
    print([type(vehicle).__name__ for vehicle in my_garage.vehicles])  # Output: ['Car', 'SportCar']
    
    # Test void_car class
    # my_vehicle = Vehicle()  # This will raise an error because Vehicle is abstract and cannot be instantiated
    # my_void_car = void_car()  # This will raise an error because void_car does not implement the abstract method start_engine()