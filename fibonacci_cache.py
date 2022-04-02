fibonacci_cache ={}
import time as tm 
start_time = tm.time()
def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1 or n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    fibonacci_cache[n] = value
    return value

for n in range(1,40):
    print(n,":" , fibonacci(n))


time_elapsed = tm.time() - start_time
print(f"time elapsed: {round(time_elapsed,10)}")    