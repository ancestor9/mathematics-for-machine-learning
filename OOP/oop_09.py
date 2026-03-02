# This code explores SOLID principles in Python using a car theme.
# 1. Demonstrates Single Responsibility by separating concerns.
# 2. Applies Open/Closed for extension without modification.
# 3. Ensures Liskov Substitution with substitutable child classes.
# 4. Uses Interface Segregation for specific interfaces.
# 5. Implements Dependency Inversion to decouple modules.
# The example uses a Car with a FuelSystem and an IVehicle interface.

from abc import ABC, abstractmethod

# 4. ISP: 인터페이스를 구체적인 기능 단위로 분리합니다.
class Movable(ABC):
    @abstractmethod
    def move(self):
        pass

class Refuelable(ABC):
    @abstractmethod
    def refill(self):
        pass

# 5. DIP & 2. OCP: 추상화된 인터페이스(IVehicle)를 정의합니다.
class IVehicle(Movable, Refuelable, ABC):
    pass

# 1. SRP: 연료 보충 로직을 별도의 클래스로 분리합니다.
class FuelSystem:
    def __init__(self, fuel_type: str):
        self.fuel_type = fuel_type

    def add_fuel(self):
        print(f"{self.fuel_type} 연료를 충전 중입니다...")

# 3. LSP: 자식 클래스들은 부모의 역할을 온전히 수행합니다.
class GasolineCar(IVehicle):
    def __init__(self):
        self.fuel_system = FuelSystem("가솔린")

    def move(self):
        print("내연기관 엔진으로 주행합니다.")

    def refill(self):
        self.fuel_system.add_fuel()

class ElectricCar(IVehicle):
    def __init__(self):
        self.fuel_system = FuelSystem("전기")

    def move(self):
        print("전기 모터로 조용히 주행합니다.")

    def refill(self):
        self.fuel_system.add_fuel()

# 고수준 모듈: 구체적인 클래스가 아닌 인터페이스(IVehicle)에 의존합니다.
class Driver:
    def drive_vehicle(self, vehicle: IVehicle):
        vehicle.refill()
        vehicle.move()

# --- 실행부 ---
if __name__ == "__main__":
    driver = Driver()
    
    # 어떤 차종이 들어와도 드라이버는 동일한 방식으로 운전 가능 (DIP & LSP)
    my_gasoline_car = GasolineCar()
    my_electric_car = ElectricCar()

    print("--- 가솔린 차 운행 ---")
    driver.drive_vehicle(my_gasoline_car)

    print("\n--- 전기차 운행 ---")
    driver.drive_vehicle(my_electric_car)