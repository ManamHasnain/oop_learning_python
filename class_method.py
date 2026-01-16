#class method is used to change the class attributes, which static method fail to do
class Person:
    name="Unknown"
    def __init__(self,name): #class attribute and instance attribute are both differnt
        self.name=name 

    #if want to change class attribute there are some ways to do it
    #way 1: use class name inside the constructor

    def __init__(self, name): #now here class attribute is being changed. name Unknown is changed to ali
        Person.name=name
    
    #second way: use __class__ which is equal to class name, above method.

    def __init__(self, name):
        self.__class__.name=name

    #third way: use @ class method a decorator which can able to change the class attributes
    @classmethod
    def __init__(cls,name): #here cls refering to the class Person
        cls.name=name


user=Person("ali")
print(user.name) #here instance attribute will be printed
print(Person.name) #here class attribute will be printed