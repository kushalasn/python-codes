class Solution:
    def mySqrt(self, x):
        #Babylonian Method
        if x<=1:
            return x
        else:
            xn=x/2
            change=1
            while(change>0.4):
                next_n=0.5*(xn+x/xn)
                change=abs(next_n-xn)
                xn=next_n
        return int(xn)        
                
                
        
        
        