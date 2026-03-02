# A class is a blueprint for creating objects in Python.
# It defines attributes (data) and methods (functions) that objects will have.
# Objects are instances created from this blueprint(class), enabling reusable code.

# property getter와 setter를 사용하여 Student 클래스에 get_info 메서드 추가
from oop_02 import Student

def getting_info(self):
    return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

Student.get_info = property(getting_info)
student1 = Student("Alice", 20, "B")
print(student1.get_info)  # Output: Name: Alice, Age: 20, Grade: B

## Car 클래스에 속성 추가 및 메서드 정의
print("\n--- Car Class with Class and Instance Attributes ---")
'''
파이썬의 **데코레이터(Decorator)**를 활용하여 
객체의 변수 접근을 제어하는 **캡슐화(Encapsulation)**의 전형적인 예시

# @property가 없는 경우
class Car:
    def __init__(self, speed):
        self._speed = speed

    def get_speed(self):        # 값을 가져오는 '함수'
        return self._speed

    def set_speed(self, value): # 값을 검사하고 저장하는 '함수'
        if value >= 0:
            self._speed = value
        else:
            print("에러!")

my_car = Car(100)

# 사용하는 사람의 코드 (복잡함)
my_car.set_speed(150)       # 괄호()를 써서 함수를 호출해야 함
print(my_car.get_speed())    # 값을 볼 때도 함수를 호출해야 함

'''
class Car:
    def __init__(self, speed):
        self.speed = speed  # Setter를 호출함

    @property
    def speed(self):
        return self._speed

    @speed.setter # 반드시 클래스 내부에 위치!
    def speed(self, value):
        if value >= 0:
            self._speed = value
        else:
            print("에러: 속도는 음수가 될 수 없습니다!")

# 실행 결과
my_car = Car(100)    # 초기값 100 설정
print(my_car.speed)
my_car.speed = 150   # 150으로 변경 성공
print(my_car.speed)
my_car.speed = -20   # "에러: 속도는 음수가 될 수 없습니다!" 출력, 값은 150 유지
print(my_car.speed)  # 출력: 150

# BankAccount 클래스에 캡슐화 적용
print("\n--- BankAccount Class with Encapsulation ---")

class BankAccount:
    def __init__(self, balance):
        self._balance = balance # 초기 잔액 설정    
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("에러: 잔액은 음수가 될 수 없습니다!")
        else:
            self._balance = amount

my_account = BankAccount(1000)
print(my_account.balance)
my_account.balance = 1500
print(my_account.balance)   

# adding deposit and withdraw methods
def deposit(self, amount):
    if amount > 0:
        self._balance += amount
        print(f"Deposited {amount}. New balance: {self._balance}")
    else:
        print("Deposit amount must be positive.")
        
def withdraw(self, amount):
    if amount > self._balance:
        print("Insufficient funds.")
    elif amount <= 0:
        print("Withdrawal amount must be positive.")
    else:
        self._balance -= amount
        print(f"Withdrew {amount}. New balance: {self._balance}")
        
BankAccount.deposit = deposit
BankAccount.withdraw = withdraw 
my_account.deposit(500)  # Output: Deposited 500. New balance: 2000
my_account.withdraw(300) # Output: Withdrew 300. New balance:
my_account.withdraw(2000) # Output: Insufficient funds.
my_account.deposit(-100) # Output: Deposit amount must be positive.

### prompt : if __name__ == "__main__" 를 사용하여 테스트 코드 작성
'''
실습과제 : A, B 은헹 계좌주인이 서로 온라인 송금하는 거래를 발생하여 각각의 잔액을 출력하는 코드를 작성하시오.(gradio 사용) 

'''

# game character class with encapsulation with property decorator
print("\n--- Game Character Class with Encapsulation ---")  
class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self._health = health
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        if value < 0:
            print("Health cannot be negative!")
        else:
            self._health = value