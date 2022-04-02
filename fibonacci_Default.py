import time as tm

start_time = tm.time()
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1,40):
    print(n,":" , fibonacci(n))
time_elapsed = tm.time() - start_time
print(f"time elapsed: {round(time_elapsed,2)}")