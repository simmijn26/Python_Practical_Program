# Q10. Second largest and second smallest without built-in functions

lst = list(map(int, input("Enter numbers separated by space: ").split()))

largest = second_largest = -999999
smallest = second_smallest = 999999

for num in lst:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Second Largest:", second_largest)
print("Second Smallest:", second_smallest)