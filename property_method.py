class Student:
    def __init__(self,phy,bio,chem):
        self.name=input("enter the name")
        self.phy=phy
        self.bio=bio 
        self.chem=chem
        # self.average=(self.phy+self.bio+self.chem)/3.0
        # self.percentage=((self.phy+self.bio+self.chem)/300)*100

    # def calculate_percentage(self):
    #     self.percentage=((self.phy+self.bio+self.chem)/300)*100
        
    
    # def calculate_average(self):  
    #     self.average=(self.phy+self.bio+self.chem)/3.0
        

    @property #here value returned will be converted into an attribute/property
    def percentage(self):
        return ((self.phy+self.bio+self.chem)/300)*100
    
    @property
    def average(self):
        return (self.phy+self.bio+self.chem)/3.0
    


stud1=Student(89,87,78)
print(stud1.average)
print(stud1.percentage)

stud1.chem=85 #we changed the marks, here marks will be changed but average and percentage still uses outdated marks to calculate percentage
#so there are two methods, one to create a differnt functions or use property method
#in first method where we create function, we first change value then call calculate_average and calculate_percentage functions which will update the value then show those value

# stud1.calculate_average()
# stud1.calculate_percentage()

#second method is used propery decorater
print(stud1.average)
print(stud1.percentage)