n=int(input("Enter number of students"))
for i in range(n):
    
    name=input("Enter Students Name: ")
    usn=input("Enter Students USN: ")

    mark1=float(input("Enter marks in course 1: "))
    mark2=float(input("Enter marks in course 2: "))
    mark3=float(input("Enter marks in course 3: "))

    total=mark1+mark2+mark3
    average=total/3
    print("-----Student Details-----") 
    print("Name:",name)
    print("USN:",usn)
    print("Course 1 Marks:",mark1)
    print("Course 2 Marks:",mark2)
    print("Course 3 Marks:",mark3)
    print("Total Marks:",total)
    print("Average Marks:",average)