class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def change_age(self, new_age):
        self.age = new_age

    @staticmethod
    def is_legal_age(age):
        return age >= 18

    @classmethod
    def create_from_string(cls, data_string):
        first_name, last_name, age = data_string.split()
        return cls(first_name, last_name, int(age))


student = Student('Егор', 'Жарский', '18')
print(student.get_full_name())
student.change_age(20)
print(Student.is_legal_age(22))
student2 = Student.create_from_string("Никита Марецкий 22")
print(student2.get_full_name())
