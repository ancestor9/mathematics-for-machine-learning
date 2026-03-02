# This code explores inheritance in Python using a car theme.
# It demonstrates how a Vehicle parent class can be inherited by Car and SportsCar
# The example includes multi-level inheritance and practical application with a Car class.

# Initial Vehicle parent class
class Vehicle:
    def __init__(self, speed):
        self.speed = speed
    def move(self):
        print("Vehicle is moving")
        
        
# Car child class with inheritance
class Car(Vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand
    def honk(self):
        print(f"Beep beep from {self.brand}!")
        
# SportsCar grandchild class with multi-level inheritance
class SportsCar(Car):
    def __init__(self, speed, brand, top_speed):
        super().__init__(speed, brand)
        self.top_speed = top_speed
        
    def move(self):
        print(f"Sports {self.brand} is racing at {self.speed} km/h!")
        
        
# Garage class for practical example
class Garage:
    def __init__(self):
        self.vehicles = []
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    def display_fastcar(self):
        for vehicle in self.vehicles:
            if vehicle.speed > 100:
                vehicle.move()
        
        
if __name__ == "__main__":
    # test vehicle class
    my_vehicle = Vehicle(80)
    print(f"My vehicle speed: {my_vehicle.speed} km/h")  # Output: My vehicle speed: 80 km/h
    my_vehicle.move()  # Output: Vehicle is moving
    
    # test car class
    my_car = Car(120, "Toyota")
    print(f"My car speed: {my_car.speed} km/h")  # Output: My car speed: 120 km/h
    my_car.move()  # Output: Vehicle is moving  
    my_car.honk()  # Output: Beep beep from Toyota!
    
    # test sports car class
    my_sports_car = SportsCar(200, "Ferrari", 350)
    print(f"My sports car speed: {my_sports_car.speed} km/h")  # Output: My sports car speed: 200 km/h
    my_sports_car.move()  # Output: Sports Ferrari is racing at 200 km/h!
    my_sports_car.honk()  # Output: Beep beep from Ferrari! 
    
    # test garage class
    my_garage = Garage()    
    my_garage.add_vehicle(my_vehicle)
    my_garage.add_vehicle(my_car)
    my_garage.add_vehicle(my_sports_car)
    print("\nAll vehicles in the garage:")
    # print only vehicles with speed > 100
    my_garage.display_fastcar()  # Output: Sports Ferrari is racing at 200 km/h!
    
    
    # 모든 차량을 하나씩 조회하여 출력하는 메서드
    def display_all_vehicles(self):
        print(f"\n==== 현재 차고지 차량 목록 ({len(self.vehicles)} 대) ====")
        
        for index, vehicle in enumerate(self.vehicles, 1):
            # 차량의 기본 정보 출력 
            # brand가 있으면 그 값을, 없으면 '일반 브랜드'라는 글자를 가져와라(브랜드가 없는 일반 Vehicle 예외 처리)
            brand = getattr(vehicle, 'brand', '일반 브랜드')
            print(f"{index}. [{type(vehicle).__name__}] 브랜드: {brand}, 현재 속도: {vehicle.speed}km/h")
            
    # Garage 클래스에 display_all_vehicles 메서드 추가
    Garage.display_all_vehicles = display_all_vehicles
       
    my_garage.display_all_vehicles()