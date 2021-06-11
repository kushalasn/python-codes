class Solution:
    def highFive(self, items):
       
        dic1=dict()
        l=[]
        
        for i in range(0,len(items)):
            dic1[items[i][0]] =[]
            
           
         
        
        for i in range(0,len(items)):
            if items[i][0] in dic1.keys():
                dic1[items[i][0]].append(items[i][1])
                
       
        for i in dic1:
         
            
            l.append([i,int(sum(sorted(dic1.get(i),reverse=True)[0:5])/5)])
            
        
        for i in range(0,len(l)):
            for j in range(i+1,len(l)):
                if l[i][0]>l[j][0]:
                    l[i],l[j]=l[j],l[i]
        
            
        return l
       
        
        
        
                
                