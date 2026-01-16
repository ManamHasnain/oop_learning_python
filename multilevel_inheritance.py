class Animal:
    def __init__(self,color):
        self.color=color
    # @ staticmethod
    def breath(self):
        print("this animal breaths")
class Mammal(Animal):
    # @staticmethod
    def walk(self):
        print("mammal walks")
class Dog(Mammal):
    def __init__(self,name,color):
        super().__init__(color)
        self.name=name
        super().walk()
        
    # @ staticmethod
    def bark(self):
        # super().walk()
        print("this dog bark woo woo!")
    
my_dog=Dog("bruno","black")
print(my_dog.name)
print(my_dog.color)
my_dog.breath()
# my_dog.walk()
my_dog.bark()