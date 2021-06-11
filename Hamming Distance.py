class Solution:
    def hammingDistance(self, x, y):
        
        
        res = 0
        for i in bin(x^y)[2:]:
            if i == '1':
                res += 1
        return res
  
        