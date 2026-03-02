#################################
# 1. 함수를 객체로 다루기 (Treating a Function Like an Object)
# 함수를 변수에 할당하고, 함수 객체의 속성에 접근하는 예제입니다.
#################################

# 1. 함수 정의
def factorial(n):
    '''n의 팩토리얼(계승)을 반환합니다. n은 음이 아닌 정수여야 합니다.'''
    return 1 if n == 0 else n * factorial(n - 1)

# 2. 함수를 변수에 할당 (일등 객체)
fact = factorial
print(f"fact(5) 결과: {fact(5)}")

# 3. 함수 객체의 속성에 접근
print(f"\n함수 이름: {fact.__name__}")
# __doc__ 속성을 사용하여 도움말 텍스트에 접근
print(f"도움말 (__doc__): {fact.__doc__}")


# 'Card' namedtuple은 이전 컨텍스트에서 정의되었다고 가정
# Card = collections.namedtuple('Card', ['rank', 'suit'])


###################################
# 2. 고차 함수와 익명 함수 (Higher-Order Functions and Anonymous Functions)
# 고차 함수는 함수를 인수로 받거나 함수를 반환하는 함수입니다.
###################################

# 데이터 리스트 (단어 길이와 문자열 자체)
data = [(10, 'apple'), (5, 'banana'), (15, 'cherry')]

# 1. 고차 함수 sorted와 익명 함수 lambda 사용
# 'key' 인수로 lambda를 사용하여, 튜플의 두 번째 요소(문자열)의 길이로 정렬
sorted_by_len = sorted(data, key=lambda item: len(item[1]))
print(f"길이로 정렬된 리스트: {sorted_by_len}")


# 2. map과 filter를 리스트 컴프리헨션으로 대체
numbers = [1, 2, 3, 4, 5, 6]

# map(lambda x: x * 2, numbers) 와 동일
doubled = [x * 2 for x in numbers]
print(f"\nmap 대체 (두 배): {doubled}")

# filter(lambda x: x > 3, numbers) 와 동일
filtered = [x for x in numbers if x > 3]
print(f"filter 대체 (3 초과): {filtered}")

#################################
# 3. 호출 가능 객체 (Callable Objects)
#################################
# __call__을 구현하여 상태를 유지하는 사용자 정의 호출 가능 객체
class Adder:
    def __init__(self, base):
        self.base = base
    
    # 이 메서드를 구현하면 인스턴스를 함수처럼 호출할 수 있습니다.
    def __call__(self, n):
        return self.base + n

# 1. 인스턴스 생성 및 상태 유지 (base=10)
add_ten = Adder(10)

# 2. 인스턴스를 함수처럼 호출
result = add_ten(5) 
print(f"add_ten(5) 호출 결과: {result}") # 출력: 15

# 3. callable() 함수로 호출 가능 여부 확인
print(f"\nAdder 인스턴스는 호출 가능한가? {callable(add_ten)}")
print(f"일반 클래스는 호출 가능한가? {callable(Adder)}")
print(f"일반 함수는 호출 가능한가? {callable(len)}")
print(f"정수 10은 호출 가능한가? {callable(10)}")