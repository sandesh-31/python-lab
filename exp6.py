while True:
    print("\n---MENU---")
    print("1. Check Even or Odd")
    print("2. Largest of Three Numbers")
    print("3. Multipliction Table")
    print("4. Prime Numbers in a Range")
    print("5. Exit")
    
    choice=input("Enter Your choice: ")
    
    if choice=="1":
        n=int(input("Enter a number: "))
        print(n,"is Even" if n%2==0 else "is Odd")
        
    elif choice=="2":
        a=float(input("Enter first number: ")) 
        b=float(input("Enter second number: "))  
        c=float(input("Enter third number: ")) 
        print("Largest number =", max(a,b,c))
        
    elif choice=="3":
        n=int(input("Enter a number: "))  
        for i in range(1, 11):
            print(f"{n} x {i} = {n*i}")
            
    elif choice=="4":
        start=int(input("Enter start of range: "))
        end=int(input("Enter end of range: "))
        print("Prime numbers:", end=" ")
        for n in range(max(2, start), end+1):
            is_prime = True
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    is_prime=False
                    break
            if is_prime:
                print(n,end=" ")
        print()
        
    elif choice=="5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")                         