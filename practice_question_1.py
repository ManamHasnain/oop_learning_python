class Student:
    def __init__(self,name,marks):
        self.name=name 
        self.marks=marks

    def average(self):
        total=0
        for val in self.marks:
            total+=val
        average=total/len(self.marks)
        print("hi ",self.name,"your total marks are ",total," and your average marks are ",average)

stud1=Student("ali",[90,85,80])
stud2=Student("hassan",[89,78,90,73])

stud1.name="hassan" #can also change name from here 
stud2.marks=[70,81,69,90] #can also change marks directly from here

stud1.average()
stud2.average()
