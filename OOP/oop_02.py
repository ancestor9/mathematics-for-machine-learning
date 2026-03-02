# A class is a blueprint for creating objects in Python.
# It defines attributes (data) and methods (functions) that objects will have.
# Objects are instances created from this blueprint(class), enabling reusable code.

# 초기 생성자 설정
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

my_car = Car("red", "Toyota")

# describe 메서드 추가
def describe(self):
    print(f"my car : {self.color} {self.model} car")

# describe 메서드를 Car 클래스에 추가
Car.describe = describe # 클래스에 메서드를 동적으로 할당

my_car.describe()  # Output: red Toyota car

def change_color(self, new_color):
    self.color = new_color
    print(f"color changed to {self.color}")

Car.change_color = change_color

my_car.change_color("blue")

# Student 클래스 정의
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def introduce(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old. My grade is {self.grade}.")
    def study(self, subject):
        print(f"{self.name} is studying {subject}.")
        
student1 = Student("Alice", 20, "A")
student1.introduce()  # Output: Hello, I'm Alice and I'm 20 years old. My grade is A.

# 학생이 공부하는 과목을 출력하는 메서드 호출
student1.study("Mathematics")  # Output: Alice is studying Mathematics.

# Add a method to update the student's grade with validation
def update_grade(self, new_grade):
    if new_grade not in ["A", "B", "C", "D", "F"]:
        print("Invalid grade. Please enter a valid grade (A, B, C, D, F).")
        return  # Exit the method if the grade is invalid
    self.grade = new_grade
    print(f"{self.name}'s grade updated to {self.grade}")

Student.update_grade = update_grade

student1.update_grade("B")  # Output: Alice's grade updated to B

# Adding get_info method to Student class
def get_info(self):
    return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

Student.get_info = get_info

print(student1.get_info())  # Output: Name: Alice, Age: 20, Grade: B

# testing edge case for grade update
student1.update_grade("E")  # Output: Invalid grade. Please enter a valid grade (A, B, C, D, F).