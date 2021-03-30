class Solution:
    def majorityElement(self, nums):
        dict_nums={}
        for i in nums:
            if i in dict_nums:
                dict_nums[i]+=1
                
            else:
                dict_nums[i]=1
                
        if dict_nums[i]>len(nums)//2:
            return i
            