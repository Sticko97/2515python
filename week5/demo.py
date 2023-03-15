#week5 & 6
import random
import json
from unittest.mock import patch, mock_open

# def add(a, b):
#     something = "stanley"
#     variable = a * 2
#     return variable + b

# for iteration in range(100):
#     num1, num2 = (random.randint(0, 100), random.randint(0,100))
#     result = add(num1, num2)


"""mocks and patches"""
# import json
# from unittest.mock import patch


# def test_function():
#     with patch("builtins.input", return_value="stanley"): #python module, requires a string
#         value = function()
#         assert value == "STANLEY"
# def function():
#     value = input("enter a value ?")
#     return value.upper()


# def test_random():
#     with patch("random.randint", return_value=50) as mock_random:
#         assert func_random() == 50
#         assert mock_random.call_count == 1
# def func_random():
#     return random.randint(0, 100)

"""using mocks and patches to fake the contents of files"""
# @patch("builtins.open", new_callable=mock_open, read_data="[]") """similar to the "with patch" method down below"""
def test_func_open():
    with patch("builtins.open", new_callable=mock_open, read_data="[]"): # if json file is not in the same folder. use the mock only if you want to mock_open the file
        content = func_open()
        assert type(content) == list
    
def func_open():
    with open("trivia.json", "r") as fp:
        content = json.load(fp)
        return content


"""
Dunder method
if it starts with __ then it is a dunder method. ex. __init__()
"""
class Example:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"Object: name is {self.name}"
    
    def __mod__(self, value):
        print("called with", value)