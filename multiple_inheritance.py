class Father:
    surname="hussain"
    def hair(self):
        print("I have black hair")
class Mother:
    def eyes(self):
        print("I have brown eyes")
class Child(Father,Mother):
    def __init__(self, name):
        self.name=name
        super().__init__()
    def height(self):
        print("I am short heighted")

child1=Child("ali")
print(child1.name)
print(child1.surname)
child1.hair()
child1.eyes()
child1.height()