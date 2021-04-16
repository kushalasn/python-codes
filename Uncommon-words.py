class Solution:
    def uncommonFromSentences(self, A, B):
        dict1={}
        print(dict1.__dir__)
        dict2={}
        a=A.split()
        b=B.split()
        p=[]
        for i in a:
            if (i in dict1):
                dict1[i]+=1
                
            else:
                dict1[i]=1
                
        for j in b:
            if (j in dict1):
                dict1[j]+=1
            else:
                dict1[j]=1
                
        for i in dict1:
            if (dict1[i]==1 and dict1[i] not in dict2):
                p.append(i)
       
       
        for i in dict2:
            if (dict2[i]==1 and dict2[i] not in dict1):
                p.append(i)
    
        
        
       
        
        return p
        
        