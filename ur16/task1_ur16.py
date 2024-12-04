import random

class Person:
    def __init__(self, name, surname, age, hobby):
        self.name = name
        self.surname = surname
        self.age = age
        self.hobby = hobby

    def greetings(self):
        print(
            f'Hello! My full name is {self.name} {self.surname} and I`m {self.age} years old. My hobby is {self.hobby}.')

class Student(Person):
    def __init__(self, name, surname, age, hobby, fav_subj, grade, grades):
        super().__init__(name, surname, age, hobby)
        self.fav_subj = fav_subj
        self.grades = grades
        self.grade = grade

    def spysaty_dz(self, copying_subj):
        if copying_subj.lower() == self.fav_subj.lower():
            print('I can give you this homework, here you are. But don`t do it the same!')
        else:
            print('I didn`t do this homework, sorry!')

class Teacher(Person):
    def __init__(self, name, surname, age, hobby, teaching_subj, salary):
        super().__init__(name, surname, age, hobby)
        self.teaching_subj = teaching_subj
        self.salary = salary

    def homework(self):
        print(f'My dear students! The homework is paragraph {random.randrange(1, 200)} exercises {random.randrange(1, 6)}-{random.randrange(7, 12)}')

my_char = Person('Viktoriia', 'Verkholat', '15', 'Drawing')
my_char.greetings()
my_classmate = Student('Lesya', 'Ukrainka', '153', 'Writing', 'Literatura', 9, 'mostly perfect')
my_classmate.spysaty_dz('Literatura')
my_teacher = Teacher('Oksana', 'Kondratyuk', '38', 'Listening to music', 'Literatura', 10000)
my_teacher.homework()

