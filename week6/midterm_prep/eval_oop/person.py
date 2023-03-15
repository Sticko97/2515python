class Person:
    def __init__(self, name, age):
        if type(name) != str or len(name) < 3:
            raise AttributeError("Name must be a string with at least three letters.")
        if type(age) != int or age < 0:
            raise AttributeError("Age must be a positive integer.")
        self.name = name
        self.age = age
        self.name_list = []
        self.age_list = []
        
    def get_name(self):
        return f"{self.name.upper()} / {self.age}"
    
