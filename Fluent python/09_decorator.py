registry = [] # 함수들이 저장될 레지스트리 (리스트)

def register(func):
    # 모듈 로드 시 이 부분이 즉시 실행됩니다.
    print(f'running register({func})') 
    registry.append(func)
    return func # 장식된 함수를 그대로 반환합니다.

@register
def f1():
    print('running f1()')
    
@register
def f2():
    print('running f2()')
    
print(f'Registry after loading module: {registry}')