# class Account:
#     __name="unknown"
#     def __init__(self, id, passwrd): #for constructor use __init__
#         self.id=id
#         self.__passwrd=passwrd

#     def reset(self):
#         return self.__passwrd
    
#     def get_details(self):
#         print(self.id)
#         print(self.__name)
#         print(self.reset())

# acc1=Account(12,"opa54")
# acc1.get_details()
# # print(acc1.reset())

# class Student:
#     __name=input("enter your name")
#     def __init__(self,grade):
#         self.__grade=grade
#     def __greet(self):
#         print(self.__name," Welcome to class!")
#     @ staticmethod
#     def college():
#         print("college name is abc college")

#     def get_info(self):
#         print(self.__name)
#         print(self.__grade)
#         self.__greet()
#         self.college()
# s=Student("A+")
# s.get_info()

#multi level inheritance concept 
# class Car:
#     @staticmethod
#     def start():
#         print("car starts")
#     @staticmethod
#     def stop():
#         print("car stops")
# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand=brand
#     def showinfo(self):
#         print("car brand : ",self.brand)

# class Fortunar(ToyotaCar):
#     def __init__(self, brand, type):
#         super().__init__(brand)
#         self.type=type
#     def showinfo(self):
#         super().showinfo()
#         print("car type : ",self.type)
# car1=Fortunar("fortunar","diesel")
# car1.start()
# car1.stop()
# car1.showinfo()


#class methods
class Student:
    college_name="abc college"
    def __init__(self,name):
        self.name=name
#another way to change class attribute
    # def change_collegename(self,new_collegeName):
    #     Student.college_name=new_collegeName
    @classmethod
    def change_collegename(cls,new_college_name):
        cls.college_name=new_college_name
stud1=Student("ali")
stud2=Student("hassan")
#both student ali and hassan belongs to abc college
print(stud1.name, "belongs to ", stud1.college_name)
print(stud2.name, "belongs to ", stud2.college_name)
print(Student.college_name)
#we want to change schoool name or we want to shift both student to another school
Student.change_collegename("xyz college")
# stud1.change_collegename("xyz college")
print(stud1.name, "belongs to ", stud1.college_name)
print(stud2.name, "belongs to ", stud2.college_name)
print(Student.college_name)


