class Solution:
    
    
    def cred(self,n):
        sum=0
        while(n!=0):
            sum=sum+n%10
            n=int(n/10)
        return sum 
    
    def most_frequent(self,List): 
        return max(set(List), key = List.count)
    
    def countBalls(self, l, h):
        lp=[]
        for i in range(l,h+1):
            t=self.cred(i)
            lp.append(t)
        return lp.count(self.most_frequent(lp))
    
    

        
            
                
           
       

            
     
    
      
    
            
            
            
            
            
        
        