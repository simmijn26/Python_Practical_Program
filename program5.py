# Q5. Separate mixed list by datatype

lst = [10, 2.5, "Hello", 3+4j, True, [1,2]]

ints = []
floats = []
strings = []
complexs = []
others = []

for i in lst:
    if type(i) == int:
        ints.append(i)
    elif type(i) == float:
        floats.append(i)
    elif type(i) == str:
        strings.append(i)
    elif type(i) == complex:
        complexs.append(i)
    else:
        others.append(i)

print("Integers:", ints)
print("Floats:", floats)
print("Strings:", strings)
print("Complex:", complexs)
print("Others:", others)