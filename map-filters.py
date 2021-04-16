def square(v):
    return v*v

def cube(v):
    return v*v*v
funcs=[square,cube]
l=[1,2,3,4,5]
for i in range(1,len(l)+1):
    val=list(map(lambda x:x(i),funcs))
    print(val)  

print("--------filter----------")
list1=[1,2,3,4,5,6,7,8,9]
def is_gret_5(v):
    return v>5

gret=list(filter(is_gret_5,list1))  
print(gret)   

print("--------reduce--------")
from functools import reduce
list2=[1,2,3,4]
prod=reduce(lambda x,y :x+y,list2)
print(prod)