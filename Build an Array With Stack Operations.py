class Solution:
    
        
        
    def buildArray(self, target, n):
        l=[]
        count=0
        for i in range(1,n+1):
            if i in target:
                l.append("Push")
            else:
                l.extend(["Push","Pop"])
            count+=1
            if (count==target[-1]):
                break
        return l        
                