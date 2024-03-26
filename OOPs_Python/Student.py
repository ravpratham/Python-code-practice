import person

class Student(person.person):

    rollno = ""
    sclass = ""

    def __init__(self, pname, gender, passion, rollno, stuclass):
        super(Student, self).__init__(pname, gender, passion)
        self.rollno = rollno
        self.sclass = stuclass

    def display(self):
        return "Student Name: ", self.name, " Gender: ", self.gender, " Passion: ", self.passion, " Rollno: ", self.rollno, " Class: ", self.sclass


s = Student("Pratham", "Male", "Music", "19", "XII-B")
print(s.display())

