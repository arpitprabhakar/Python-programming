class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __str__(self):
        return f"Student(name={self.name}, roll={self.roll})"

print(Student)
