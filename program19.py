# Q19. Demonstrate iterators

lst = input("Enter elements separated by space: ").split()

it = iter(lst)

print("Iterator Output:")

for i in range(len(lst)):
    print(next(it))