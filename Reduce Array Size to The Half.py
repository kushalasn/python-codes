class Solution:
    def minSetSize(self, arr):
        counts=collections.Counter(arr)
      
        countz=[number for count,number in counts.most_common()]
        #print(countz)
      
       
        countz.sort(reverse=True)
        count=0
        step=0
        
        for i in countz:
            count+=i
            step+=1
            if (count>=(len(arr)//2)):
                break
        return step        
                
       
            
            
        
        
        
        
            
              
        
        