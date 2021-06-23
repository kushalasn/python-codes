class Solution:
    def maxCoins(self, p):
        maxi=0
        p.sort(reverse=True)
        while(len(p)!=0):
            p.remove(p[0])
            p.pop()
            maxi+=p[0]
            p.remove(p[0])
            
            
        return maxi    
