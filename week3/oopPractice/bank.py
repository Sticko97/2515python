class BankAccount:
    def __init__(self, amount=0):
        self._amount = amount #this attribute is static, you can call whatever you want. No one outside of the class should use it
                              # they should use the property
                              # b._amount is invalid, it has to be self._amount
    def deposit(self, value):
        self._amount += value
        
    
    def withdraw(self, value):
        if value > self._amount:
            raise AttributeError

        self.deposit(-value)

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value): #this is a setter function, sets an attribute to our object
        if value < 0:
            raise AttributeError
        self._amount = value