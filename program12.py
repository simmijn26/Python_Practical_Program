# Q12. Remove duplicates while maintaining order

lst = input("Enter elements separated by space: ").split()

result = []

for item in lst:
    if item not in result:
        result.append(item)

print("List after removing duplicates:", result)