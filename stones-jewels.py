class Solution:
    def numJewelsInStones(self, jewels, stones):
        st_a_jw=0
        for i in stones:
            for j in jewels:
                if i==j:
                    st_a_jw+=1
                
        return st_a_jw    
        