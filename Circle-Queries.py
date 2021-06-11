import math
class Solution:
    def countPoints(self, points, queries):
        answer=[]
        
        for j in queries:
            count=0
            for p in points:
                if abs(math.sqrt((j[0]-p[0])*(j[0]-p[0])+(j[1]-p[1])*(j[1]-p[1]))) <= j[2]:
                    count+=1
            answer.append(count) 
         
        return answer
         
                
        