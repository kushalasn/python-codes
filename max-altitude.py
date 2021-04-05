class Solution:
    def largestAltitude(self, gain):
        r_ng=len(gain)
        alt_point=[]
        for i in range(1000):
            alt_point.append(0)
    
        for  i in range(1,r_ng+1):
            alt_point[i]=alt_point[i-1]+gain[i-1]
            
            
        return max(alt_point)    
            
            
        
        