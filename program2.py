# Q2. Mutable and Immutable

x = int(input("Enter integer: "))
print("Before:", x, id(x))
x = x + 5
print("After:", x, id(x))

lst = [1,2,3]
print("Before list:", lst, id(lst))
lst.append(4)
print("After list:", lst, id(lst))