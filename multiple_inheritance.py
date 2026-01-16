class Father:
    surname="hussain"
    def __init__(self,salary):
        self.salary=salary
    def hair(self):
        print("I have black hair")
class Mother:
    def eyes(self):
        print("I have brown eyes")
class Child(Father,Mother):
    def __init__(self, name, salary):
        self.name=name
        super().__init__(salary)
        super().hair()


    def height(self):
        print("I am short heighted")

father=Father(19000)
print(father.salary)
child1=Child("ali",10000)
print(child1.name)
print(child1.salary)
print(child1.surname)
child1.hair()
child1.eyes()
child1.height()
