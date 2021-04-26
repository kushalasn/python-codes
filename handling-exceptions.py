x=input("enter  number1  ")
y=input("enter  number2  ")
try:
    z=x/int(y)
except Exception as e:
    print("exception occured-",type(e).__name__)
    z='not possible'

print("Divison is-",z)