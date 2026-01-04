#unlike OOP in C++ here making attribute or method private is little different, method given below:

class Account:
    __name=input("enter your name") #here name is private attribute and can only used within class


    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no #here is account no is public as we can use it outside the class as well
        self.__acc_pass=acc_pass  #to make an attribute private we use __ two underscore before it, and now it is not accessible outside class, only within class

    def reset_password(self): #we use a different function to access account password
        return self.__acc_pass
    
    def __welcome(self):
        print("welcome to your account",self.__name)

    def user_info(self):
        self.__welcome()
        print(self.acc_no)
        print(self.reset_password())

account_no=input("enter your account no")
account_password=input("enter your account password")
acc1=Account(account_no,account_password)
print(acc1.acc_no)
# print(acc1.__acc_pass) #we can't print it as this is an private attribute
print(acc1.reset_password())
acc1.user_info()


