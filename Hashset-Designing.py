class MyHashSet:

    def __init__(self):
        self.size=10000
        self.table=[None]*self.size
    
    
    def calculate_hashvalue(self,key):
        return key%self.size
        
        

    def add(self, key):
        hv=self.calculate_hashvalue(key)
        if self.table[hv]==None:
            self.table[hv]=[key]
        else:
            self.table[hv].append(key)
        
        

    def remove(self, key):
        hv=self.calculate_hashvalue(key)
        
        if self.table[hv]!=None:
            while key in self.table[hv]:
                self.table[hv].remove(key)
        
        

    def contains(self, key):
        hv=self.calculate_hashvalue(key)
        if self.table[hv]==None:
            return False
        else:
            if key in self.table[hv]:
                return True
            else:
                return False
       
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)