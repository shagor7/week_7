class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.age = None
        self.marks = None

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")

    def setAge(self, age):
        self.age = age

    def setMarks(self, marks):
        self.marks = marks


if __name__ == "__main__":
    student = Student("Shagor", 101)
    student.setAge(22)
    student.setMarks(88)
    student.display_info()
