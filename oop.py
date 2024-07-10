class Myclass: # initialization of class
    x=21 
    rollNo='2K19CSUN01119'
    branch='CSE'
    def __init__(self,name,age): # constructor in python
        self.name=name
        self.age=age
abc = Myclass('Amar',100) # object creation 
print(abc.name) 
print(abc.age)
print(abc.x)   # accessing class properties
# del abc.name # we can delete that property
# del abc # we can whole object, after doing this, if we call then it will say not defined 
