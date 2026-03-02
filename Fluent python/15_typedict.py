from typing import TypedDict, List
from pydantic import BaseModel, Field

# 1. TypedDict로 OrderItem 정의 (Pydantic 모델은 아님, 순수 타입 힌트)
class OrderItem(TypedDict):
    """단일 주문 항목의 스키마를 정의하는 TypedDict"""
    product_id: int
    quantity: int
    price: float

# 2. Pydantic BaseModel을 사용하여 복잡한 구조 정의
class Order(BaseModel):
    """주문 전체를 나타내는 Pydantic 모델"""
    order_id: int = Field(..., description="고유 주문 ID")
    customer_name: str
    
    # TypedDict를 포함하는 List로 타입 힌트 (중첩 구조)
    items: List[OrderItem] 
    
    total_amount: float
    is_shipped: bool = False

print("\n" + "="*15 + " TypedDict를 사용한 Pydantic 결과 " + "="*15)

# 유효한 데이터 생성
valid_order_data = {
    "order_id": 101,
    "customer_name": "Eve",
    "items": [
        {"product_id": 501, "quantity": 2, "price": 10.50},
        {"product_id": 502, "quantity": 1, "price": 25.00}
    ],
    "total_amount": 46.00
}

try:
    order_instance = Order(**valid_order_data)
    print("✅ Pydantic 인스턴스 생성 및 검증 완료.")
    print(f"주문 ID: {order_instance.order_id}, 항목 수: {len(order_instance.items)}")
    
except ValidationError as e:
    print(f"❌ 오류 발생: {e}")