# Q3. All Operators

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Arithmetic:", a+b, a-b, a*b, a/b, a%b, a**b, a//b)
print("Relational:", a>b, a<b, a==b, a!=b)
print("Logical:", a>0 and b>0, a>0 or b>0, not(a>b))
print("Bitwise:", a&b, a|b, a^b, ~a, a<<1, a>>1)

a += b
print("Assignment += :", a)