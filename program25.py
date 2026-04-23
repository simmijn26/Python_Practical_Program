# Q25. Class variable vs Instance variable

class Student:
    school = "AI University"   # class variable

    def __init__(self, name):
        self.name = name       # instance variable

s1 = Student("Simmi")
s2 = Student("Riya")

print(s1.name, s1.school)
print(s2.name, s2.school)