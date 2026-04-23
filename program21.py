# Q21. Fibonacci recursive and iterative with time

import time

n = int(input("Enter n: "))

def fib_rec(x):
    if x <= 1:
        return x
    return fib_rec(x-1) + fib_rec(x-2)

start = time.time()
print("Recursive:", fib_rec(n))
print("Recursive Time:", time.time() - start)

start = time.time()

a, b = 0, 1
for i in range(n):
    a, b = b, a + b

print("Iterative:", a)
print("Iterative Time:", time.time() - start)