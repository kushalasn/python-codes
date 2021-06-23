import math
def mean(array,n):
    sum=0
    for i in range(0,n):
        sum=sum+array[i]
    return sum/n
def cov(array1,array2,n):
    sum=0
    for i in range(0,n):
        sum=sum+(array1[i]-mean(array1,n))*(array2[i]-mean(array2,n))

    return sum/(n-1)

arr1 = [65.21, 64.75, 65.26, 65.76, 65.96]
n = len(arr1)
 
arr2 = [67.25, 66.39, 66.12, 65.70, 66.64]
m = len(arr2)    

if(m==n):
    print(cov(arr1,arr2,n))