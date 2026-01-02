class Student:
    college="abc college" #class attribute
    def __init__(self,fullname,marks):
        self.name=fullname
        self.mark=marks 
    
    def welcome(self):
        print("welcome student, ",self.name)
    
    def get_marks(self):
        return self.mark
    
name1=input("enter the name of student 1")
mark1=int(input("enter the total marks of student 1"))
name2=input("enter the name of student 2")
mark2=int(input("enter the total marks of student 2"))

stud1=Student(name1,mark1)
stud2=Student(name2,mark2)

print(Student.college)
stud1.welcome()
print(stud1.get_marks())

print(Student.college)
stud2.welcome()
print(stud2.get_marks())