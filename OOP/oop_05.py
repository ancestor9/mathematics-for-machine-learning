# This code explores polymorphism in Python using a car theme.
# It demonstrates how different vehicle classes can share a common interface (move) with unique behaviors.
# The example includes practical application with a RaceTrack class.

# Initial Vehicle parent class
class Vehicle:
    def __init__(self, speed):
        self.speed = speed
    def move(self):
        print("Vehicle is moving")
        
# Car child class with custom move behavior
class Car(Vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand
    def move(self):
        print(f"{self.brand} car is driving at {self.speed} km/h!")
        
# SportsCar child class with custom move behavior
class SportsCar(Vehicle):
    def __init__(self, speed, brand, top_speed):
        super().__init__(speed)
        self.brand = brand
        self.top_speed = top_speed
    def move(self):
        print(f"{self.brand} sports car is racing at {self.speed} km/h!")
        
# RaceTrack class to demonstrate polymorphism
class RaceTrack:
    def __init__(self):
        self.vehicles = []
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    def start_race(self):
        for vehicle in self.vehicles:
            vehicle.move()  
        

if __name__ == "__main__":
    # test vehicle class        
    my_vehicle = Vehicle(80)
    print(f"My vehicle speed: {my_vehicle.speed} km/h")  # Output: My vehicle speed: 80 km/h
    my_vehicle.move()  # Output: Vehicle is moving
    
    # test car class
    my_car = Car(120, "Toyota")
    print(f"My car speed: {my_car.speed} km/h")  # Output: My car speed: 120 km/h
    my_car.move()  # Output: Toyota car is driving at 120 km/h!
    
    # test sports car class
    my_sports_car = Car(200, "Ferrari")
    print(f"My sports car speed: {my_sports_car.speed} km/h")  # Output: My sports car speed: 200 km/h
    my_sports_car.move()  # Output: Ferrari car is driving at 200 km/h!
    
    # test race track with polymorphism
    race_track = RaceTrack()
    race_track.add_vehicle(my_vehicle)
    race_track.add_vehicle(my_car)
    race_track.add_vehicle(my_sports_car)       
    print("\n--- Starting the race! ---")
    race_track.start_race()  # Output: Vehicle is moving
    
