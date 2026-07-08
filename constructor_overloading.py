#constructor overlaoding through default parameter
class Student:
    def __init__(self, name="unkown", age="unknown", department="not assigned"):
        self.name=name
        self.age=age
        self.department=department
    def showInfo(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Department : ",self.department)
stud1=Student()
stud1.showInfo()

stud2=Student("ali")
stud2.showInfo()

stud3=Student("muhammad",12)
stud3.showInfo()

stud4=Student("hassan",18,"cs")
stud4.showInfo()

# constructor overloading via @classmethod 
class Student:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    @classmethod
    def from_string(cls,data):
        name,age=data.split(",")
        return cls(name,int(age))
    def showInfo(self):
        print("Name : ",self.name)
        print("Age : ",self.age)

# stud=Student()
stud=Student.from_string("ali,20")
stud.showInfo()

#constructor overloading via *arg method
class Student:
    def __init__(self, *arg):
        print(arg)
stud=Student("ali")
stud1=Student("hassan",23)
stud2=Student("muhammad",19,"cs")

#*args constructor overloading in detail
class Student:
    def __init__(self,*args):
        if len(args)==1:
            self.name=args[0]
            self.age=None
        elif len(args)==2:
            self.name=args[0]
            self.age=args[1]
        else:
            print("invalid number of arguments")
    def showInfo(self):
        print("name : ",self.name)
        print("age : ",self.age)
stud1=Student("ali")
stud1.showInfo()
stud2=Student("ali",20)
stud2.showInfo()
stud3=Student('ali',20,"cs")
