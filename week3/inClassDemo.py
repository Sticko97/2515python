"""
Object is a variable, but it does more than just holding a value
You can call functions on the object
"""

class Example:
    #classes are containers, when we create an object from that container we get an instance called a method?
    def __init__(self, hello):
        print("hello world")
        self.hello = hello

    def hello(self, text2, text3="herro"):
        print(self.text)
        print(text2)
        print(text3)
        pass

"""python creates a new object using the class Example as a template"""
# obj = Example()
# type(obj)