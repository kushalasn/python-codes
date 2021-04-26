class Solution:
    def missingNumber(self, nums) :
        nums_list=set(nums)
        n=len(nums)+1
        for i in range(n):
            if i not in nums_list:
                return i
            
            
            

    
    
# Awesome xor answer  

class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing    
            