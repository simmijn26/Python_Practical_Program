# Q9. All list operations

lst = []

n = int(input("How many elements initially? "))
for i in range(n):
    lst.append(input("Enter element: "))

print("Original List:", lst)

lst.append(input("Append element: "))
print("After append:", lst)

lst.insert(int(input("Insert position: ")), input("Insert value: "))
print("After insert:", lst)

lst.extend(input("Enter elements to extend (space separated): ").split())
print("After extend:", lst)

lst.remove(input("Enter element to remove: "))
print("After remove:", lst)

lst.pop()
print("After pop:", lst)

lst.sort()
print("After sort:", lst)

lst.reverse()
print("After reverse:", lst)
