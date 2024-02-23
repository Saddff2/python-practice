class BankAccount:
    def __init__(self, name, id, balance):
        self.name = name
        self.id = id
        self.balance = balance
        self.customers = {}
        
    def deposit(self, amount):
        self.customers[self.balance] += amount
        print('Your transaction was successful', f'Your {self.customers}')
        
    def withdraw(self, amount):
        self.balance -= amount
        print('Your transaction was successful')

    def get_balance(self):
        return f'Your balance is {self.balance}'
    
    def __str__(self):
        return f'Hi {self.name}, your balance is {self.balance}, your account number is {self.id}.'
    
daniel = BankAccount('Daniel', 343342434, 10000)

daniel.deposit(1000)
daniel.deposit(121235)
daniel.withdraw()