class Solution:
    def heightChecker(self, heights):
        expected=sorted(heights)
        count=0
        for i in range(0,len(heights)):
            if (expected[i]!=heights[i]):
                count+=1
        return count       
                
    def heightChecker(self, heights):
        return sum(h1!=h2 for h1,h2 in zip(heights,sorted(heights)))
                    