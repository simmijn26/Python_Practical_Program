# Q1. Built-in data types, type and memory location

a = int(input("Enter integer: "))
b = float(input("Enter float: "))
c = input("Enter string: ")
d = complex(input("Enter complex number (e.g. 2+3j): "))
e = input("Enter True/False: ") == "True"

data = [a, b, c, d, e, [1,2], (1,2), {1,2}, {"x":1}]

for i in data:
    print("Value:", i, "Type:", type(i), "Memory:", id(i))