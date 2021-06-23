class Publication:
    def __init__(self,title,price):
        self.title=title
        self.price=price


class Periodical(Publication):
    def __init__(self, title, price,period,publisher):
        super().__init__(title, price)
        self.period=period
        self.publisher=publisher

class Book(Publication):
    def __init__(self,title,author,pages,price):
        super().__init__(title,price)
        self.title=title
        self.author=author
        self.pages=pages
        self.price=price

class Magazine(Periodical):
    def __init__(self,title,publisher,price,period):
        super.__init__(title,price,period,publisher)
       
class Newspaper(Periodical):
    def __init__(self,title,publisher,price,period):
        super.__init__(title,price,period,publisher)
        

b1=Book("Brave New World","Chroma",100,20)
print(b1.author)        
