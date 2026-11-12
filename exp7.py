def fact(n):
    if n<0:
        return None
    result=1
    for i in range(2,n+1):
        result=result*i
    return result
n=int(input("enter a number:"))
factorial=fact(n)
if fact is None:
    print("factorial is not defined")
else:
    print("factorial=",factorial)
def simpint(p,t,r=5):
    simpleinterst=(p*t*r)/100
    return simpleinterst
#using default rate
p=int(input("enter principle amount"))
t=int(input("enter a number"))
print("simple interst(default rate 5%)=",simpint(p,t))
square=lambda x:x*x
num=int(input("enter a number"))
print("square of a number is:",square(num))
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "division is not define for zero devisor"
    return a/b

import mymath
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition =", mymath.add(a, b))
print("Subtraction =", mymath.sub(a, b))
print("Multiplication =", mymath.mul(a, b))
print("Division =", mymath.div(a, b))    