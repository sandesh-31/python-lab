num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

print("Addition=",num1+num2)
print("Multiplication=",num1*num2)

if num2 !=0:
    print("Division=",num1/num2)
    print("Floor Division=",num1//num2)
    print("Modulus=",num1%num2)
else:
    print("Division,floor division and modulus are undefined for zero divisor.") 
    
print("Exponentiation=",num1**num2) 