"""

def__init__(self)
-constructor
_special type of Method which is getting called when we are creating an Object
_which we can use intilize the class Properties as well
_self is a mandatory paramter and being passed automaticaly





you need to know
self.name
self.roll
self.branch

represent the instance properties
and

def __init__(self,name,roll,branch)
i.e all the parameters which we are passing for those instance properties
"""

class student:
    def __init__(self,name,gender,age):
        print("constructor is being called")
        self.name=name
        self.gender=gender
        self.age=age




s1=student('ankit','male',12)



""" 
_along with condtructor
_we can aslo create some instance methods in a class
_and all the instance method will have a self as a mandatory parameter

Like for student we will have instance methods to 
_getrollNumber
_getname
_getMakrs

"""
class stud:

   def __init__(self,name,roll,branch):
       self.name=name
       self.branch=branch
       self.roll=roll

   def getname(self):
       return self.name

   def getrollNumber(self):
       return self.roll

   def getbranch(self):
       return self.branch




s2=stud("Aniket",121,"ME")
print(s2.getname())
print(s2.getrollNumber())
print(s2.getbranch())



"""" 
in Python we cannot have multiple constructors
Default ->has only single parameter which is self

def __init__(self):



and parametrize 
def __init__(self,name,roll,brnach):



at same time

if we have added 2 constructor
then
1___
2__


2und one will be considered valid
"""

""""---------------------Attributes--------------------------------------------------------"""
""" 
Attributes is simply a Properties
we have two types of perperties
1_class
atrr belong to class
_for all the instances the class attribute will be the same

eg what could be the same for all the Diffrent student  Object

collageName
branch
city


those will be the same for all the Object so we will Declare it as a class Attr






2_Instance
atrr belong to instance
_for all the instances the instance attribute will be the Unique or Diffrent    

are those which is Diffrent for all the Instances of that class
eg
name
roll
Gender
Marks



"""



class stu:
    collageName="ACS collage" #class atrr

    def __init__(self,name,roll,branch):
        self.name=name
        self.branch=branch
        self.roll=roll




"""
we can aslo access the class properties via instance of a class or className itself
"""

s3=stu("Aman",1223,"ME")
print(s3.branch)
print(s3.roll)
print(s3.name)

print(stu.collageName)


