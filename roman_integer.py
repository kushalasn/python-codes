class Solution:
    def romanToInt(self, str):
        set={'I' :1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        l=len(str)
        count=0
        i=0
        while (i <len(str)):
            c1=set[str[i]]
            if (i+1<len(str)):
                
                c2=set[str[i+1]]
                if (c1<c2):
                    count=count-c1
                    i=i+1
                     
                else:
                    count=count+c1
                    i=i+1
                    
            else:
                count=count+c1
                i=i+1
           
                
        return count       