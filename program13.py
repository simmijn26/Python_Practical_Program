# Q13. Dictionary of students and marks

n = int(input("Enter number of students: "))
students = {}

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

print("Student Dictionary:", students)

topper = max(students, key=students.get)
print("Topper:", topper, "-", students[topper])

avg = sum(students.values()) / len(students)
print("Average Marks:", avg)

sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)

print("Sorted by Marks:")
for name, marks in sorted_students:
    print(name, ":", marks)