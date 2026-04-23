# Q20. Manual map(), filter(), reduce()

nums = list(map(int, input("Enter numbers: ").split()))

# map -> square
mapped = []
for i in nums:
    mapped.append(i * i)

print("Map (square):", mapped)

# filter -> even numbers
filtered = []
for i in nums:
    if i % 2 == 0:
        filtered.append(i)

print("Filter (even):", filtered)

# reduce -> sum
total = 0
for i in nums:
    total += i

print("Reduce (sum):", total)