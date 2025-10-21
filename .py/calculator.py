a=int(input("ENTER NO OF TIME YOU WANT TO USE CALCULATOR :- "))
for x in range(a):
    n1=int(input("Enter 1st number :-"))
    n2=int(input("Enter 2nd number :-"))
    c=input("which operation you need to perform give its symboll :-")
    if c=="+":
        print(n1+n2)
    elif c=="-":
        print(n1-n2)
    elif c=="*":
        print(n1*n2)
    elif c=="/":
        print(n1/n2)
    elif c=='**':
        print(n1**n2)
    else:
        print((n1)**(1/2),(n2)**(1/2))
