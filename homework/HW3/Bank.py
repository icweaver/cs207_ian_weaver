from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankAccount():
    
    def __init__(self, owner, accountType):
        self.owner = owner
        self.accountType = accountType
        self.balance = 0 # start with zero balance for new accounts
        
    def withdraw(self, amount): 
        if amount > self.balance:
            print('Insufficient funds.')
        elif amount < 0:
            print('Must withdraw positive amount.')
        else:
            self.balance -= amount
    
    def deposit(self, amount):
        if amount <= 0: 
            print('Please enter a positive amount.')
        else:
            self.balance += amount
        
    def __str__(self):
        return(f"Account owner: {self.owner}\n"
               f"Account type : {self.accountType.name}")
        
    def __len__(self):
        return self.balance

class BankUser():
    
    def __init__(self, owner):
        self.owner = owner
        self.accounts = {}
    
    def addAccount(self, accountType):
        if accountType.name not in self.accounts.keys():
            account = BankAccount(self.owner, accountType) 
            self.accounts[accountType.name] = account
        else:
            # don't add duplicate account
            print(f"{accountType.name} already created")
        
    def getBalance(self, accountType):
        if accountType.name in self.accounts.keys():
            balance = self.accounts[accountType.name].__len__()
            print(f"Balance: {balance}")
        else:
            print(f"Account not created")
    
    def deposit(self, accountType, amount):
        if accountType.name in self.accounts.keys():
            print('in here')
            self.accounts[accountType.name].deposit(amount)
        else:
            print(f"Account not created")
        
    def withdraw(self, accountType, amount):
        if accountType.name in self.accounts.keys():
            self.accounts[accountType.name].withdraw(amount)
        else:
            print(f"Account not created")
    
    def __str__(self):
        print(f"Account owner: {self.owner}")
        for account_type, account in self.accounts.items():
            print(f"{account_type}: ${account.__len__()}")
def ATMSession(bankUser):
    def Interface():
        def main_exit():
            print('Exiting session...')
            return False
            
        def main_create_account():
            return bankUser.addAccount(accountType)
    
        def main_check_balance():
            bankUser.getBalance(accountType)
            
        def main_deposit():
            deposit_amount = int(input('Deposit amount:'))
            bankUser.deposit(accountType, deposit_amount)
            
        def main_withdraw():
            withdrawal_amount = int(input('Withdrawal amount:'))
            bankUser.withdraw(accountType, withdrawal_amount)
        
        # print options of menu dictionary
        def print_menu(menu):
            for option_num, option in menu.items():
                print(f'{option_num}){option}\n')
        def print_main():
            main = {1:'Exit', 2:'Create Account', 3:'Check Balance', 
                       4:'Deposit', 5:'Withdraw'}
            print('Enter Option:\n')
            print_menu(main)  
            print()
        def print_sub():
            sub = {1:'Checking', 2:'Savings'}
            print_menu(sub)
        
        # main menu
        menu_main = {'1':main_exit, 
                     '2':main_create_account,
                     '3':main_check_balance, 
                     '4':main_deposit,
                     '5':main_withdraw} 
        loop = True
        while(loop or loop==None): 
            print()
            print_main() # print main menu
            # read user input to main menu
            input_main = input()
            if input_main == '1': 
                loop = menu_main[input_main]()
            elif input_main in menu_main.keys():
                try:
                    print_sub()  # print sub menu
                    input_sub = input() # read user input to sub menu
                    if input_sub == '1':
                        accountType = AccountType.CHECKING
                        loop = menu_main[input_main]() # run sub-menu
                    elif input_sub == '2':
                        accountType = AccountType.SAVINGS
                        loop = menu_main[input_main]() # run sub-menu
                    else: 
                        print('Not valid input')
                        loop = True # go back to main menu
                except KeyError:
                    print('Not valid input')
                    loop = True # just go to main menu again
            else:
                print('Not valid input')
                loop = True # return to main menu
    return Interface

# Closure
user = BankUser('Mr. Foo')
atm = ATMSession(user)
atm()
