class Solution:
    def shortestToChar(self, s, c):
        l=[]
        answers=[]
        print(answers)
        for i in range(len(s)):
            if s[i]==c:
                l.append(i)
                print(l)
        for  i in range(len(s)):
            p=[]
            for j in range(len(l)):
                p.append(abs(i-l[j]))
                
         
            answers.append(min(p))
            p.clear()
            
        return answers    
              
  
                