class Solution:
    def climbStairs(self, n) :
        steps=[0,1,2]
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        else:
            for i in range(3,n+1):
                steps.append(self.climbStairs(i-1)+self.climbStairs(i-2))
        return steps[-1]        
                
            