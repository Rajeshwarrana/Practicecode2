print(" ")
print(" ")
print("                                            ☀☀ ÚñÌ† ÇÖñVÈR†ÖR ☀☀ ")
print(" ")  
print(" ")
q=int(input("                            ENTER HOW MANY TIME YOU WANT TO RUN UNIT CONVERTOR\n                                            \n                                            "))
print(" ")
print(" ")
for s in range(q):
    n=int(input("Enter Number To Be converted {IN CENTIMETERS} :- "))
    print(" ")
    y=input("                                      CHOOSE  'm' for meter\n                                      CHOOSE  'y' for yard\n                                      CHOOSE  'ml' for mile\n                                      CHOOSE  'i' for inch\n                                      CHOOSE  'km' for kilometer\n                                      CHOOSE  'mm' for millimeter\n                                      CHOOSE  'fe' for feet\n  ⁂  ")
    print(" ")
    print(" ")
    if y=="m":
        print("VALUE IN METERS IS :- ",n/100,"meters")
    elif y=="mm":
        print("VALUE IN MILLIMETERS IS :- ",n*10,"millimeters")
    elif y=="y":
        print("VALUE IN YARDS IS :- ",n*0.01093613,"yards")
    elif y=="i":
        print("VALUE IN INCHES IS :- ",n*0.3937008,"inches")
    elif y=="km":
        print("VALUE IN KILOMETERS IS :- ",n*0.00001,"kilometers")
    elif y=="fe":
        print("VALUE IN FEETS IS :- ",n*0.0328084,"feet")
    elif y=="ml":
        print("VALUE IN MILES IS :- ",n*0.00000006214,"mile")
    else:
        pass
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")

