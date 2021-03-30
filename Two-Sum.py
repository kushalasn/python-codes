class Solution:
    def twoSum(self, nums, target):
        
        cmap={}
        for idx,val in enumerate(nums):
            if val not in cmap:
                cmap[val]=idx
            if (target-val) in cmap and idx!=cmap[target-val]:
                return [idx,cmap[target-val]]