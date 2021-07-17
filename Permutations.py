class Solution:
    def permute(self,nums):
        if (len(nums)==1):
            return [nums]
        if (len(nums)==2):
            n0,n1=nums[0],nums[-1]
            return [[n0,n1],[n1,n0]]
        else:
            result=[]
            for i in range(0,len(nums)):
                temp=nums[:i]+nums[i+1:]
                for j in self.permute(temp):
                    result.append([nums[i]]+j)          
        return result            
                
            
        