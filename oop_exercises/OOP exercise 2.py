# Write a Python program to create a person class. 
# Include attributes like name, country and date of birth. 
# Implement a method to determine the person's age.

class Person:
    def __init__(self,name:str, country:str, birth:int):
        self.name = name
        self.country = country
        self.birth = birth
    
    def get_age(self):
        return 2024 - self.birth
    
    def __str__(self):
        return f'Hi {self.name}, you live in {self.country}, your age is {self.birth}'
 
daniel = Person('Daniel', 'Israel', 2001)

print(daniel)
print(daniel.get_age())
