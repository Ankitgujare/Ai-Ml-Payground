class animal:
    @staticmethod
    def eat():
        print("eating....")


class Dog(animal):
    animal.eat()


class person:
    name="Rohan"
    age=12


class student(person):

    @staticmethod
    def getstudentData():
        print(f"name is {person.name} and age is {person.age}")



s1=student
s1.getstudentData()

class vehicle:

    @staticmethod
    def start():
        print("Vehical started")


class Car(vehicle):
    vehicle.start()


class Parent:
    def __init__(self):
        print("Iam a default constructor")

class Child(Parent):
    print("Iam child")




x=Child


class BankAccount:
    AccountNumber=121212121
    Balence=10_0000

    @classmethod
    def displayBalence(Cls):
        print(f"Account Number {Cls.AccountNumber} and Balence is {BankAccount.Balence}")


class SavingAccount(BankAccount):
    @staticmethod
    def display_interest():
        print("Intrest rate:7")




v=SavingAccount
v.displayBalence()
v.display_interest()

""""
 whenever Parent class Constructor needs any parameter to
 Initlizes its properties its child class Responsibility 
 to Provides those paramters to the parent class
 To do that we use the 
 super() -->call
 
 lets take an example
 """


class A:

    def __init__(self,amount):
        self.amount=amount
        print(f"recived an Amount {amount}")








class B(A):

    def __init__(self,amount):
        super().__init__(amount)
        print("Iam constructor of B")




b1=B(121)



"""
Questions for you 
can we have multiple constructors in a class 
is it possible
"""











