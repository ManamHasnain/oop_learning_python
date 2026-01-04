class Student:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    
    @staticmethod
    def college():
        print("ABC College")
    
    @staticmethod
    def welcome():
        print("welcome student!")

s1=Student("ali",18)
s2=Student("hassan",32)

print(s1.name)
print(s1.age)
s1.college()
s1.welcome()

#using del keyword, to delete an object and some of it's properties
s2.welcome() #will get welcome student!
print(s2.age)
del s2.age #now we can't access age as it is also being deleted
# print(s2.age) #get error student has no attribute age
del s2 #now whole object is being deleted,can't access anything
