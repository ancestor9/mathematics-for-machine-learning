import time
import threading
import multiprocessing
import asyncio
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from typing import NoReturn

# ----------------- 1. 공통 블로킹 함수 -----------------

def blocking_io_task(delay: int) -> str:
    """I/O 집약적 작업을 흉내내는 블로킹 함수"""
    print(f"[{threading.current_thread().name}] I/O 작업 시작 ({delay}초)...")
    time.sleep(delay)  # I/O 대기를 흉내내며 GIL을 해제함
    print(f"[{threading.current_thread().name}] I/O 작업 완료.")
    return f"I/O 결과({delay})"

# ----------------- 2. 스레드를 사용한 동시성 (I/O 집약적) -----------------

def run_with_threads():
    """threading을 사용하여 I/O 작업을 동시에 실행합니다."""
    print("\n=== 스레드 동시성 시작 ===")
    start = time.perf_counter()
    
    # 두 개의 스레드를 생성하여 블로킹 함수 실행
    t1 = threading.Thread(target=blocking_io_task, args=(3,), name="Thread-1")
    t2 = threading.Thread(target=blocking_io_task, args=(2,), name="Thread-2")
    
    t1.start()
    t2.start()
    
    t1.join() # 완료될 때까지 메인 스레드 블로킹
    t2.join()
    
    end = time.perf_counter()
    print(f"=== 스레드 동시성 완료 (총 {end - start:.2f}초) ===")


# ----------------- 3. 프로세스 풀을 사용한 병렬성 (CPU 집약적) -----------------

def cpu_intensive_task(n: int) -> bool:
    """CPU 집약적 작업을 흉내내는 함수 (예: 소수 판별)"""
    print(f"  [프로세스 {multiprocessing.current_process().pid}] CPU 작업 시작...")
    # 매우 큰 숫자의 소수 판별 (오래 걸림)
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def run_with_process_pool():
    """concurrent.futures.ProcessPoolExecutor를 사용하여 CPU 작업을 병렬 실행합니다."""
    print("\n=== 프로세스 병렬성 시작 (GIL 우회) ===")
    start = time.perf_counter()
    tasks = [99999999999997, 99999999999989] # 두 개의 큰 소수 후보
    
    # ProcessPoolExecutor를 사용하여 여러 코어에서 작업 분산
    with ProcessPoolExecutor() as executor:
        results = executor.map(cpu_intensive_task, tasks)
        
    for task, result in zip(tasks, results):
        print(f"  {task}는 소수인가? {result}")
        
    end = time.perf_counter()
    print(f"=== 프로세스 병렬성 완료 (총 {end - start:.2f}초) ===")


# ----------------- 4. 코루틴을 사용한 비동기성 (이벤트 루프) -----------------

async def async_io_task(delay: float) -> str:
    """I/O 대기를 await로 양보하여 이벤트 루프를 차단하지 않습니다."""
    print(f"  [코루틴] I/O 작업 시작 ({delay}초)...")
    await asyncio.sleep(delay) # await을 사용하여 제어권을 이벤트 루프에 양보
    print(f"  [코루틴] I/O 작업 완료.")
    return f"Async 결과({delay})"

async def run_with_coroutines():
    """asyncio.gather를 사용하여 코루틴을 동시에 실행합니다."""
    print("\n=== 코루틴 비동기성 시작 ===")
    start = time.perf_counter()
    
    # asyncio.gather는 여러 awaitable 객체를 동시에 실행하고 결과를 리스트로 반환
    results = await asyncio.gather(
        async_io_task(3),
        async_io_task(2)
    )
    
    end = time.perf_counter()
    print(f"=== 코루틴 비동기성 완료 (총 {end - start:.2f}초) ==꿈")


# ----------------- 5. 실행 함수 -----------------

if __name__ == "__main__":
    # GIL이 해제되어 3초와 2초의 I/O 작업이 약 3초만에 완료됨
    run_with_threads() 
    
    # CPU 집약적 작업이 병렬로 실행됨
    run_with_process_pool()
    
    # 메인 진입점. 3초와 2초의 I/O 작업이 약 3초만에 완료됨
    asyncio.run(run_with_coroutines())