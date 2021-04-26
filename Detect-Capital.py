class Solution:
    def detectCapitalUse(self, word):
        if word.isupper()==True:
            return True
        
        if word.islower()==True:
            return True     
                
        if (ord(word[0])>=65) and (ord(word[0])<=94):
            if word[1:].islower()==True:
                return  True
            else:
                return False