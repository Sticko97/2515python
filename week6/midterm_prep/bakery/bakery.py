class Bakery:
    def __init__(self, name):
        self.name = name
        self.croissants = 0
        self.money = 0
        
    def bake(self, number_of_croissants=0):
        self.number_of_croissants = number_of_croissants
        if isinstance(number_of_croissants, int) and number_of_croissants > 0:
            self.croissants += number_of_croissants
        elif isinstance(number_of_croissants, str) and number_of_croissants.isnumeric():
            self.croissants += int(number_of_croissants)
        else:
            raise ValueError
    
    def sell(self, number_of_croissants=1):
        if isinstance(number_of_croissants, int) and number_of_croissants > 0:
            if self.croissants >= number_of_croissants:
                self.croissants -= number_of_croissants
                self.money += number_of_croissants * 3
            else:
                raise RuntimeError("You cannot sell more croissants than you have")
        else:
            raise ValueError("The number of croissants to sell must be a positive integer")
        
    def __str__(self):
        return self.name
    