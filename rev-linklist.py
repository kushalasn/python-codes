class Node:
    def __init__(self,data):         #node creation
        self.data=data
        self.ref=None
    
class Linklist:                       #root node creation
    def __init__(self,head):
            
            
            self.head=head

    def printlist(self):
        if self.head is None:
            print("list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref




node1=Linklist(100)
node1.printlist()            
    