class Book:
    def __init__(self,title,author,pages,price):
        self.title=title
        self.author=author
        self.pages=pages
        self.price=price


    def getprice(self):
        if hasattr(self,"_discount"):
            return self.price-(self.price*self._discount) #objects are the only parameters for this case
        else:
            return self.price

    def setdiscount(self,percentage):
        self._discount=percentage    
#__double underscore makes it a private attribute
#_single underscore is  meant for internal use, and the name of the attribute may change
b1=Book("War and Peace","Bond",1000,150)
#b2=Book("The catch in the bye")     
print(b1.getprice())
b1.setdiscount(0.30)
print(b1.getprice())

