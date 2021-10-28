'''
Inheritance:
 used to extend class
inherts all the methods and properties from another class
'''

class Demo():

    def __init__(self, x, y): #Init is used for initialization and is invoked without any call, when object is created
        print("Hello",x,y)
        self.x = x
        self.y = y
    def display(self):
        print("Hi")
    def __str__(self):
        return "It's an object of Class Demo "

class B(Demo):
    '''Inheriting Demo CLass
    Demo is super class
    B is sum Class
    '''

    def info(self):
        print("Class B")
    def display(self):
        print("CCCCCCCCCCCCCCCCCCc")
j = B(6, 7)
# print(j)
j.display()
j.info()