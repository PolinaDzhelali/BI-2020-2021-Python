x=float(input())
op=input()
y=float(input())
if op=='+': 
    result=x+y 
elif op=='-': 
    result=x-y
elif op=='*': 
    result=x*y
elif y!=0: 
    if op=='/': 
        result=x/y
elif y==0: 
    result="division by zero!"
print(result)




