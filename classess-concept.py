class Laptop:
    def __init__(self,company,model,colors):
        self.company=company
        self.model=model
        self.colors_available=colors
    def is_laptop_available(self,color):
        return color   in  self.colors_available

laptop = Laptop('Dell', 'inspiron 7000', ['Silver', 'Black'])

if laptop.is_laptop_available('Silver'):
    print("Available")
else:
     print("Not available")
        

if laptop.is_laptop_available('Green'):
    print("Available")
else:
     print("Not available")

import random

print(random.__file__ )  
