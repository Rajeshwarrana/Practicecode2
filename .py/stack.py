lis=[]
while True:
    i=input("1-->PUSH\n2-->POP\n3-->DISPLAY\n4-->EXIT\n        :-")
    if i=="1":
        print()
        print()
        val=input("ENTER VALUE TO ENTER :- ")
        print()
        print()
        lis.append(val)
        print("ITEM ADDED !! ")
    elif i=="2":
        if len(lis)==0:
            print()
            print()
            print("N0 ITEM FOUND IN LIST !!")
            print()
            print()
        else:
            lis.pop()
    elif i=="3":
        for x in lis:
            print()
            print()
            print(x)
    elif i=="4":
        print()
        print()
        print("THANKS !! ")
        break
    
        
        
        
