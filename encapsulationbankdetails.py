class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance
        
    def deposit(self, amount):
        if amount > 0:
                self.__balance += amount
                print(f"${amount} deposited successfully!")
        else:
            print("Invalid deposit amount!")
            
            
    def withdraw(self, amount):  
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn seccussfully!")
        else:
            print("Insufficient balance or invalid amount!")
            
    def get_balance(self):
        return self.__balance
    
account = BankAccount("Ray", 1000)
account.deposit(500)
account.withdraw(300)
print(f"Current balance: ${account.get_balance()}")