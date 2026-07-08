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


class Car:
    @staticmethod
    def start():
        print("car starts")
    @staticmethod
    def stop():
        print("car stops")
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand
    def showinfo(self):
        print("car brand : ",self.brand)

class Fortunar(ToyotaCar):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type=type
    def showinfo(self):
        super().showinfo()
        print("car type : ",self.type)
car1=Fortunar("fortunar","diesel")
car1.start()
car1.stop()
car1.showinfo()

        