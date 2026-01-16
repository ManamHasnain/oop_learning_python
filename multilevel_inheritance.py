class Animal:
    # @ staticmethod
    def breath(self):
        print("this animal breaths")
class Mammal(Animal):
    # @staticmethod
    def walk(self):
        print("mammal walks")
class Dog(Mammal):
    def __init__(self,name):
        self.name=name
        
    # @ staticmethod
    def bark(self):
        super().walk()
        print("this dog bark woo woo!")
    
my_dog=Dog("bruno")
print(my_dog.name)
my_dog.breath()
# my_dog.walk()
my_dog.bark()