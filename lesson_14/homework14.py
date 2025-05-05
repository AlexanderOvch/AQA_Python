class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        self.average_grade = new_grade

    def print_info(self):
        print(f"Ім'я: {self.name}")
        print(f"Прізвище: {self.surname}")
        print(f"Вік: {self.age}")
        print(f"Середній бал: {self.average_grade}")


student1 = Student("Іван", "Петренко", 20, 4.3)

print("Інформація про студента до зміни:")
student1.print_info()

new_grade_input = input("\nВведіть новий середній бал студента: ")

try:
    new_grade = float(new_grade_input)
    student1.update_average_grade(new_grade)
except ValueError:
    print("Помилка: потрібно ввести число!")

print("\nІнформація про студента після зміни:")
student1.print_info()
