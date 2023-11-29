import copy

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def display_info(self):
        print(f"Студент: {self.name}, Вік: {self.age}, Спеціальність: {self.major}")

class StudentPrototype:
    def __init__(self, prototype):
        self.prototype = prototype

    def clone(self, name, age):
        cloned_student = copy.deepcopy(self.prototype)
        cloned_student.name = name
        cloned_student.age = age
        return cloned_student

original_name = input("Введіть ім'я студента: ")
original_age = int(input("Введіть вік студента: "))
original_major = input("Введіть спеціальність студента: ")

original_student = Student(original_name, original_age, original_major)
prototype = StudentPrototype(original_student)

num_clones = int(input("Скільки клонів студента ви хочете створити? "))
clones = []

for i in range(1, num_clones + 1):
    clone_name = input(f"Введіть нове ім'я для клону №{i}: ")
    clone_age = int(input(f"Введіть новий вік для клону №{i}: "))
    cloned_student = prototype.clone(clone_name, clone_age)
    clones.append(cloned_student)

print("\nІнформація про оригінального студента:")
original_student.display_info()

print("\nІнформація про клонованих студентів:")
for i, clone in enumerate(clones, 1):
    print(f"\nІнформація про клон №{i}:")
    clone.display_info()
