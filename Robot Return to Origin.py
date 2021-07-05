class Solution:
    def judgeCircle(self, moves):
        dic1=dict()
        for i in moves:
            if i in dic1:
                dic1[i]+=1
            if i not in dic1:
                dic1.update({i:1})    
        print(dic1)
        if((dic1['R']==dic1['L']) and (dic1['D']==dic1['U'])):
            return True
        else:
            return False