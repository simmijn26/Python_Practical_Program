# Q11. Tuple packing and unpacking with nested tuples

a = input("Enter first value: ")
b = input("Enter second value: ")
c = input("Enter third value: ")

t = (a, b, (c, "Nested"))

print("Packed Tuple:", t)

x, y, (z, n) = t

print("Unpacked Values:")
print("x =", x)
print("y =", y)
print("z =", z)
print("n =", n)