from customer import Customer

class Account(Customer):
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        if not isinstance(owner, Customer):
            raise AttributeError("owner must be Customer")
        
    def deposit(self, amount):
        """
        receives a float argument: the amount to be deposited. 
        If the argument is negative, raise a AttributeError exception.
        it adds the deposited amount to the account amount
        """
        if amount < 0: #money in account cant be negative
            raise AttributeError("Cannot deposit negative amount")
        self.amount += amount
        
    def withdraw(self, amount):
        """
        it receives a float argument: the amount to be withdrawn.
        If the argument is negative, raise a AttributeError exception.
        it removes the amount provided from the account
        """
        if amount < 0:
            raise AttributeError("Cannot withdraw no amount")
        self.amount -= amount
        
    def transfer(self, account, amount):
        """
        it has two arguments: account and amount
        it must raise a TypeError exception if the account is not an instance of Account
        the method withdraws amount from the current instance and deposits it into the account
        """

        if not isinstance(account, Account):
            raise AttributeError("Not your account")
        self.withdraw(amount)
        account.deposit(amount)
    
class CreditAccount(Account):
    def __init__(self, customer, interest):
        super().__init__(customer)
        self.interest = interest

    def compute_interest(self):
        if self.amount < 0:
            self.amount *= (100 + self.interest) / 100
            self.amount -= 10

class SavingsAccount(Account):
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        if amount < 0:
            raise UserWarning("A savings account cannot be less than 0$")
        self._amount = amount
    