import time
from typing import Callable, Any

def measure_time(func: Callable, *args, **kwargs) -> Any:
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()

    excution_time = end - start
    print(f"執行時間: {excution_time:.8f} 秒")

    if excution_time <= 2:
        print("✅ 執行時間在 2 秒內")
    else:
        print("❌ 執行時間超過 2 秒")

    return result