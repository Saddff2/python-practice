class BankAccount:
    def __init__(self, name:dict, id:int, money:float, commision=0.1):
        self.name = name
        self.id = id
        self.money = money
        self.commision = commision
        self.customers = {}
        
    def create_account(self, id, money=0):
        if id in self.customers:
            print('Account already exists')
        else:
            self.customers[id] = money
            print('Account created successfuly')
    
    def deposit(self, id, number):
        if id in self.customers:
            self.customers[id] += number
            print(f'Added successfuly, your balance is {self.money}')
        else:
            print('Account does not exist')
    
    def take_credit(self, credit):
        return self.money + credit/0,9
    
    def send_money(self, number, commision):
        return self.money - number/(1-commision)
    
    def __str__(self):
        return f'Hi {self.name} balance account is {self.money}, your id is {self.id}, your commision for transactions is {self.commision*100}%'
    
daniel = BankAccount(name = 'Daniele', id=342523530, money=12000, commision=0.1)
nadav = BankAccount(name = 'Nadav', id=342530593, money=11111, commision=0.2)

print(nadav)
print(daniel)
