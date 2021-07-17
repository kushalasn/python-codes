# from itertools import combinations
# class Solution(object):
#     def triangleNumber(self, nums):
#         count=0
#         for i in tuple(combinations(nums,3)):
#             if (sum(sorted(i)[:2])>sorted(i)[-1]):
#                 count+=1
#         return count            
#Built in toolcase


class Solution(object):
    def triangleNumber(self, nums):
        count=0
        nums=sorted(nums)
        for i in range(2,len(nums)):
            l=0
            r=i-1
            while(l<r):
                if(nums[l]+nums[r]>nums[i]):
                    count+=(r-l)
                    r-=1
                else:
                    l+=1
        return count            