class Solution:
    def xorOperation(self, n, start):
        nums=[]
        
        v=0
        for i in range(n):
            nums.append(start+2*i)
            print(nums[i],end=' ')
            v=v^nums[i]
            
        return v    
            
        
        