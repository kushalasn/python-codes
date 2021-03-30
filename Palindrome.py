class Solution:
    def isPalindrome(self, p):
        if p<0:
            return False
        else:
            s=str(p)
            a=int(s[::-1])
            if a==p:
                return True
            else:
                return False
            