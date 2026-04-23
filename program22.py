# Q22. Create module for factorial and prime checking

# Save as mymodule.py
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True