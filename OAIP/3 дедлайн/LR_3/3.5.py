import time
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def tail_fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return tail_fibonacci(n - 1, b, a + b)
n = 35

start_time = time.time()
result_naive = fibonacci(n)
end_naive = time.time() - start_time
print(f"Fibonacci({n}) = {result_naive}")
print(f"Time taken (Naive): {end_naive:.6f} seconds")

start_time = time.time()
result_tail = tail_fibonacci(n)
end_tail = time.time() - start_time
print(f"Tail Fibonacci({n}) = {result_tail}")
print(f"Time taken (Tail): {end_tail:.6f} seconds")