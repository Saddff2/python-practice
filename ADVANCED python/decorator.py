import pprint

class MyDate:
    
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


    @classmethod
    def from_string(cls,a):
        l = a.split("/")
        return cls(l[0],l[1],l[2])
    
    @staticmethod
    def do_something2(a,b):
        return a+b
    
    def __str__(self):
        return f'{self.day}, {self.month}, {self.year}'
        
    def do_something(self, t):
        print(f"I was here {str(t)}")
        


x = MyDate.do_something2(1,2)
print('static method returns', x)
    
my_date = MyDate(1,1,1)


nadav_date = r'1/1/2021'
my_date.do_something(nadav_date)

nadav_date1 = MyDate.from_string(nadav_date)
print(nadav_date1)


