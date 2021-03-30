class Solution:
    def reverse(self, x):
        print(x)
        if x>0:
            x_p=list(str(x))
            x_pp=x_p[::-1]
            x_f=[str(i) for i in x_pp]
            x_ff=int(''.join(x_f))
            print(x_ff)
            if x_ff >=-2147483648 and x_ff <= 2147483647:
                return x_ff
            else:
                return 0
            
            
            
        if x<0:
            x=-x
            x_p=list(str(x))
            x_pp=x_p[::-1]
            x_f=[str(i) for i in x_pp]
            x_ff=int(''.join(x_f))
            print(x_ff)
            x_ff=-x_ff
            print(x_ff)
            if x_ff >=-2147483648 and x_ff <= 2147483647:
                return x_ff
            else:
                return 0
        else:
            return 0
        
            
      
        
        
        