from customer import Customer
from account import Account, CreditAccount, SavingsAccount

class Bank:
    def __init__(self, name):
        """
        Constructor - Initializes the main attributes of a Bank 
        """
        self.name = name
        self.accounts = {}
        
    def create_account(self, category, owner, interest=0):
        """
        Method to create a bank account
        """
        if not isinstance(owner, Customer):
            raise TypeError("Owner must be instance of Customer Class")

        if category == "account":
                account = Account(owner)
        elif category == "credit":
            account = CreditAccount(owner, interest)
        elif category == "savings":
            account = SavingsAccount(owner, interest)
        else:
            raise ValueError("category must be either 'account', 'credit', or 'savings'")

        self.accounts[account] = owner
        return account
        

    def find_accounts(self, ssn):
        """Method returns the list of account(s) associated with the given customer"""
        if not isinstance(ssn, Customer):
            raise TypeError("Customer SSN Invalid")
        return [account for account, account_ssn in self.accounts.items() if account_ssn == ssn]

    @property
    def balance(self):
        return sum(account.amount for account in self.accounts.keys())
    
    def find_accounts_by_ssn(self, ssn:str):
        """
        """
        pass
    
    def find_accounts_by_name(self, name:str):
        pass
        

        
        
        
        