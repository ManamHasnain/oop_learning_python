#abstraction: hiding the implementation details from the user and showing only neccesary information

#here in this example how car is started and stopeed hidden from user, only we show him that car has started or stopped
class Car:
    def __init__(self):
        self.brk = False
        self.acc= False
        self.clutch =False

#this showing first all break, accelerator, clutch were at zero meaning False
#then first clutch pressed, it becomes True, then acceletor pressed it also becomes True then message printed car has started
    def start(self): 
        self.clutch= True
        self.acc= True
        print("car has started")
#when we apply breaks, brk become True and message printed car has stopped
    def stop(self):
        self.brk=True
        print("car has stopped")

my_car=Car()
my_car.start()
my_car.stop()

#here all detail like how car has started or how stopped hidden from user__abstraction.