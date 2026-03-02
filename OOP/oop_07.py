# This code explores encapsulation in Python using a car theme.
# It demonstrates how to protect data using naming conventions and methods.

# Vehicle parent class with encapsulation
class Vehicle:
    def __init__(self, speed):
        self._speed = speed
    def set_speed(self, speed):
        if speed >= 0:
            self._speed = speed
    def get_speed(self):
        return self._speed
    
# Car child class with encapsulation
class Car(Vehicle):
    def __init__(self, speed):
        super().__init__(speed)
        self.__fuel_level = 0  # Car 클래스에서 정의됨
    def add_fuel(self, amount):   
        if amount >= 0:
            self.__fuel_level += amount
            
# test section to match script demonstration
if __name__ == "__main__":
    # test vehicle class 
    my_vehicle = Vehicle(80)
    print(f"My vehicle speed: {my_vehicle.get_speed()} km/h")  # Output: My vehicle speed: 80 km/h

    # test car class
    my_car = Car(120)
    print(f"My car speed: {my_car.get_speed()} km/h")  # Output: My car speed: 120 km/h
    my_car.set_speed(150)       
    print(f"My car speed: {my_car.get_speed()} km/h")  # Output: My car speed: 150 km/h
    my_car.add_fuel(50)
    print(f"My car fuel level: {my_car._Car__fuel_level}")  # Output: My car fuel level: 50 (Note: Accessing private variable using name mangling)