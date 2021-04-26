class Solution:
    def canBeEqual(self, target, arr):
        target.sort()
        arr.sort()
        if target==arr:
            return True
        else:
            return False