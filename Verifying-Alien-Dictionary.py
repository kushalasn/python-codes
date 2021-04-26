
class Solution:
    def isAlienSorted(self, words, order):
        

        d=dict()
        for k,v in enumerate(order):
            d[v]=k
       
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j>=len(words[i+1]):
                    return False
                if words[i][j]!=words[i+1][j]:
                    
                    if d[words[i][j]]>d[words[i+1][j]]:
                        return False
                    break
        return True
                
            