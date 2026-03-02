# This code explores composition in Python using a car theme.
# It demonstrates how to build complex objects from simpler ones.
# The example uses a Car composed of Engine and Wheel components.

# Engine class as a component
class Engine:
    def __init__(self, power): # Initializes the engine with power
        self.power = power
    def start(self):
        print(f"Engine starting with {self.power} HP")
    def stop(self):
        print("Engine stopped")
        
# Wheel class as a component
class Wheel:
    def __init__(self, size):  # Initializes the wheel with size
        self.size = size
    def rotate(self):
        print(f"Wheel rotating at {self.size} inches")
        
# Car class composed of Engine and Wheels
class Car:  
    def __init__(self, engine, wheels):
        self.engine = engine
        self.wheels = wheels
    def start(self):
        self.engine.start()
    def stop(self):
        self.engine.stop()
    def rotate_wheels(self):
        for wheel in self.wheels:
            wheel.rotate()
            
# Test section to match script demonstration
if __name__ == "__main__":  
    # Create engine and wheels
    my_engine = Engine(150)
    my_wheels = [Wheel(16), Wheel(16), Wheel(16), Wheel(16)]
    
    # Create car with composition
    my_car = Car(my_engine, my_wheels)
    
    # Test car functionality
    my_car.start()  # Output: Engine starting with 150 HP
    my_car.rotate_wheels()  # Output: Wheel rotating at 16 inches (repeated for each wheel)
    my_car.stop()  # Output: Engine stopped