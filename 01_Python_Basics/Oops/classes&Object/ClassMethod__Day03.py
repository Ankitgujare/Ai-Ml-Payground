""""
Type of methods
we have 3 type of methods
1.instance
2.Class
3.static

here we will talk about the Instance method

What is intance method
_Are those method which takes (self) as a compulary parameter

"""


class student:
    CollageName="ABCD"

    def __init__(self,name,roll,branch):
        self.roll=roll
        self.name=name
        self.branch=branch


    def getStudentInfo(self):
        print("name ",self.name)
        print("RollNumber ",self.roll)
        print("Branch ",self.branch)
        print("Collage Name ",self.CollageName)


""" 
and as you can see in the instance method 
we can aslo access the class Attributes

so do you remember what is class Attributes
"""



"""
----------------------------------------------------------------------------------------------------------------------------------------
"""

"""
Now lets talk about the class Methods

as a instance methods take a self as a compulsory parameter
Likewise class methods takes class (Cls) as a compulsory Parameter
and with the help of class methods we can only access the class Attributes
Not an Instance Attributes

lets see how its Look Like
"""

class Phone:
    manufactuing="India"
    def __init__(self,brand,ram,color):
        self.brand=brand
        self.color=color
        self.ram=ram


    @classmethod
    def manufaturing(Cls):
        print(Cls.manufactuing)






p1=Phone
p1.manufaturing()
Phone.manufaturing()


""""
always remember we can Only call the class properties in the class method
and not Object Properties if we have tried we will error
"""
"""
 what is Decatators
 @classmethods
"""




"""" 
----------------------------------------------------------------------
"""

"""
What is static function

Are those which neither take self or class as parameter


__To create a static function we will use the decorators which is 
@static method 
which convert  Our normal functions into the static method

static fun 
-dosent belong to class
-dosent belong to instances

they are stand alone function which is there in a class

why we create static methods in a class if its dosent belong to class?  
Ans->static methods ar tied up with the classes
"""
class laptop:


    @staticmethod
    def calculateDiscount(originalPrice,Discount):
        finalPrice=originalPrice-(Discount*originalPrice/100)
        print("Price to Pay",finalPrice)



laptop.calculateDiscount(10_000,10)


""""
As You have seen we have not used any instance or class Attrr
and ie the idea behind the Static Method

to convert Our Normal functions into static funs we use the
@staticmethod decorators
"""










