import datetime
class Bank:
    __bank_name = 'Bro Bank Pvt Ltd'
    __interest_rate = 10

    def __init__(self, f_name, l_name, user_age, balance=0):
        self.first_name = f_name
        self.last_name = l_name
        self.age = user_age 
        self.balance = balance
      
    def get_current_blance(self):
        print(f'The current balance is {self.balance}')

    def add_balance(self, deposit_balance):
        if deposit_balance > 0:
            self.balance = self.balance + deposit_balance
            print('Your amount has been deposited successfully.')
            self.get_current_blance()
        else:
            print('Enter a valid amount.')
    
    def withdraw_balance(self, withdraw_amount):
        if withdraw_amount > self.balance or withdraw_amount < 0:
            print('Hait tarika. k para ho yesto.')
            print(f'You can withdraw only upto {self.balance}')
        else:    
            self.balance = self.balance - withdraw_amount

    @classmethod
    def get_bank_name(cls):
        return cls.__bank_name
    
    @classmethod
    def get_interest_rate(cls):
        print(f'The current interest rate is {cls.__interest_rate}')

    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.__interest_rate = new_rate
        Bank.get_interest_rate()

    @classmethod
    def get_bank_name(cls):
        return Bank.__bank_name
    
    @classmethod
    def get_interet_rate(cls):
        print(f'The current interest rate is {cls.__interest_rate}')
    
    @staticmethod
    def get_holiday_list():
        print('Yaaaaayyyyyyyyy :) :) :) ')
        print('Teej ma sab kt haru lai bidaa cha')
        print('Dashain holidays last from ghatasthapana to purnima')
        print('Tihar ma Laxmi puja ako din deki Bhai tika ko voli palta samma bidaaaaaa')

while True:
    print('*' * 30)
    print(f'Welcome to {Bank.get_bank_name()}')
    user_account = None
    try:
        user_choice = input('Enter 1 to open bank account.\nEnter 2 to check current balance.\nEnter 3 to deposit balance.\nEnter 4 to withdraw balance.\nEnter 5 to check current interest rate.\nEnter 6 to change the inerest rate.\nEnter 7 to check holiday list:  ')
        if user_choice == '1':
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            user_age = int(input('Enter age: '))
            user_account = Bank(first_name.upper(), last_name.upper(), user_age)
            
            current_hour = datetime.datetime.now().hour

            greetings = 'Good morning' if current_hour >= 0 and current_hour < 12 else 'Good Afternoon' if current_hour >= 12 and current_hour < 17 else 'Good evening'

            print(f'{greetings} Mr. {user_account.first_name.strip()} {user_account.last_name.strip()}. Your account has been created successfully.')

        elif user_choice == '2' and user_account != None:
            user_account.get_current_blance()

        elif user_choice == '3' and user_account != None:
            balance = int(input('Enter deposit amount: '))
            user_account.add_balance(balance)

        elif user_choice == '4' and user_account is not None:
            user_account.get_current_blance()
            amount = int(input('Enter withdraw amount: '))
            user_account.withdraw_balance(amount)
        
        elif user_choice == '5' and user_account is not None:
            Bank.get_interest_rate()

        elif user_choice == '6' and user_account is not None:
            print('WARNING')
            print('Only change the interest rate with the permission of the manager and the deicision from Bro Advisory Board.')
            user_input = input('Enter 1 to continue 0 to exit: ') 
            if user_input == '1':
                new_rate = int(input('Enter the new interest rate: '))
                Bank.set_interest_rate(new_rate)
            else:
                continue
        elif user_choice == '7' and user_account is not None:
            Bank.get_holiday_list()
        
        if user_account is None:
            print('Please create an account first before proceeding.')
    except:
        print('Please create an account first before proceeding.')