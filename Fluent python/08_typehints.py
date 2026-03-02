from typing import Optional, Union, List, Tuple
from collections.abc import Mapping

# Python 3.9+ 에서는 List[int] 대신 list[int] 사용 가능
# 여기서는 하위 버전 호환성을 위해 typing.List 사용 (혹은 from __future__ import annotations)

# Optional 및 Union
def greeting(name: str, enthusiasm: Optional[int] = None) -> str:
    # Optional[int]는 Union[int, None]과 동일
    if enthusiasm is None:
        return f"Hello, {name}."
    return f"Hello, {name}!" * enthusiasm

# 제네릭 컬렉션 및 고정 길이/가변 길이 튜플

def process_records(data: List[Tuple[str, int]],  # 리스트에 str과 int 튜플 포함
                    settings: Mapping[str, Union[str, int]], # dict 대신 Mapping ABC 사용
                    coordinates: Tuple[float, float, float] # 고정 길이 3차원 좌표
                    ) -> Tuple[int, ...]: # 가변 길이 정수 튜플 (int, int, ...) 반환
    
    """레코드를 처리하고, 처리된 항목 수와 좌표를 반환합니다."""
    
    processed_count = len(data)
    
    # Mapping 사용으로 dict, OrderedDict 등 다양한 맵핑 타입 허용
    print(f"설정 타입: {type(settings)}")
    
    # 반환 타입: 가변 길이 튜플 (여기서는 간단히 정수 카운트를 반환)
    return (processed_count, 1, 2)


greeting_result = greeting("Alice", 3)
print(greeting_result)
records = [("item1", 10), ("item2", 20)]
settings = {"mode": "fast", "retry": 3}
coordinates = (1.0, 2.0, 3.0)
processed = process_records(records, settings, coordinates)
print(f"처리된 항목 수: {processed}")

###############################
# 4. 고급 타입 힌트 (Advanced Type Hints)
###############################
from typing import Any
from typing import TypeVar, Hashable, Callable, NoReturn, Protocol

# 1. TypeVar 및 bound 매개변수
# TypeVar T는 Hashable(해시 가능한) 타입을 상한선으로 가짐
H = TypeVar('H', bound=Hashable)

def get_hash(item: H) -> int:
    """입력 타입과 동일한 타입을 반환하지 않고, 단순히 hash 값을 반환."""
    return hash(item)

# 2. 정적 프로토콜 (typing.Protocol)
class SupportsLessThan(Protocol):
    """< 연산자를 지원하는 모든 타입을 정의하는 프로토콜"""
    def __lt__(self, other: Any) -> bool: ...

def find_min(items: List[SupportsLessThan]) -> SupportsLessThan:
    """< 연산자를 지원하는 리스트에서 최솟값을 찾습니다."""
    # 정렬이나 min() 함수는 내부적으로 __lt__에 의존
    return min(items)

# 3. Callable (다른 함수를 인수로 받음)
Callback = Callable[[int, int], float] # 인수는 (int, int), 반환은 float

def calculate_with_callback(a: int, b: int, func: Callback) -> float:
    """두 정수를 콜백 함수에 전달하고 결과를 반환."""
    return func(a, b)

def divide(x: int, y: int) -> float:
    return x / y

result = calculate_with_callback(10, 5, divide)
print(f"\nCallable 사용 결과: {result}")

# 4. NoReturn
def emergency_exit(code: int) -> NoReturn:
    """이 함수는 절대 정상적으로 종료되지 않고 프로세스를 종료합니다."""
    import sys
    sys.exit(code)
    # 이 이후의 코드는 실행되지 않음 (타입 검사기에게 알려줌)