#python program to build Restaurant Menu using Class i
# print("hello")

class MyString:
    def __init__(self, value):
        self._value = value

    def __len__(self):
        return len(self._value)

string = MyString("Hello World")
print(len(string)) #11
