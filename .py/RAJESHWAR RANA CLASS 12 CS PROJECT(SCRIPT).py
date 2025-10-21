print(" ")
print(" ")
print("                                            ☀☀ ÚñÌ† ÇÖñVÈR†ÖR ☀☀ ")
print(" ")  
# WE NEED TO CHOOSE WHICH TYPE OF UNIT WE NEED TO CONVERT ___
print(" ")
print("CHOOSE length\nCHOOSE weight\nCHOOSE time\nCHOOSE area\nCHOOSE money\n")
print(" ")  
print(" ")
y = input("WHICH QUANTITY YOU WANT TO CONVERT CHOOSE in lower letters {ABOVE GIVEN} :-  ")
print(" ")  
print(" ")
print(" ")  
print(" ")

# NO OF TIME CODE WILL RUN
q = int(input("ENTER HOW MANY TIMES YOU WANT TO RUN UNIT CONVERTOR  :-  "))
print(" ")
print(" ")  
print(" ")

# PROGRAM WILL ACCORDING TO USERS CHOICE
# LET SAY USER HAD TO CONVERT VALUES OF DISTANCE THAN USE WILL CHOOSE LENGTH
# FOR TIME CONVERSION USER WILL CHOOSE TIME
# FOR WEIGHT CONVERSION USER WILL CHOOSE WEIGHT
while True:
    if y.lower() == "length":  # making it case-insensitive
        for _ in range(q):
            n = int(input("Enter Number To Be converted {IN CENTIMETERS} :- "))
            print(" ")
            y = input("                                      CHOOSE  'm' for meter\n                                      CHOOSE  'f' for foot\n                                      CHOOSE  'y' for yard\n                                      CHOOSE  'ml' for mile\n                                      CHOOSE  'i' for inch\n                                      CHOOSE  'km' for kilometer\n                                      CHOOSE  'mm' for millimeter\n  ⁂  ")
            print(" ")
            print(" ")
            if y == "m":
                print("VALUE IN METERS IS :- ", n / 100, "meters")
            elif y == "mm":
                print("VALUE IN MILLIMETERS IS :- ", n * 10, "millimeters")
            elif y == "f":
                print("VALUE IN FOOTS IS :- ", n * 0.0328084, "foot")
            elif y == "y":
                print("VALUE IN YARDS IS :- ", n * 0.01093613, "yards")
            elif y == "i":
                print("VALUE IN INCHES IS :- ", n * 0.3937008, "inches")
            elif y == "km":
                print("VALUE IN KILOMETERS IS :- ", n * 0.00001, "kilometers")
            elif y == "fe":
                print("VALUE IN FEETS IS :- ", n * 0.0328084, "feet")
            elif y == "ml":
                print("VALUE IN MILES IS :- ", n * 0.00000006214, "mile")
            else:
                pass
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
    elif y.lower() == "weight":  # Making it case-insensitive
        for _ in range(q):
            n = int(input("Enter Number To Be converted {IN KILOGRAMS } :- "))
            print(" ")
            y = input("                                      CHOOSE  'g' for gram\n                                      CHOOSE  't' for toone\n                                      CHOOSE  'he' for hectogram\n                                      CHOOSE  'de' for decagram\n                                      CHOOSE  'deci' for decigram\n                                      CHOOSE  'mi' for milligram\n  ⁂  ")
            print(" ")
            print(" ")
            if y == "g":
                print("VALUE IN GRAMS IS :- ", n * 1000, "grams")
            elif y == "t":
                print("VALUE IN TOONES IS :- ", n * 0.001, "toone")
            elif y == "he":
                print("VALUE IN HECTOGRAM IS :- ", n * 10, "hectograms")
            elif y == "de":
                print("VALUE IN DECAGRAM IS :- ", n * 100, "decagrams")
            elif y == "deci":
                print("VALUE IN DECAGRAM IS :- ", n * 10000, "decigrams")
            elif y == "mi":
                print("VALUE IN MILLIGRAMS IS :- ", n * 1000000, "milligrams")
            else:
                pass
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
    elif y.lower() == "time":  # Making it case-insensitive
        for _ in range(q):
            n = int(input("Enter Number To Be converted {IN HOURS } :- "))
            print(" ")
            y = input("                                      CHOOSE  'm' for minute\n                                      CHOOSE  'd' for day\n                                      CHOOSE  'w' for weeks\n                                      CHOOSE  'mo' for months\n                                      CHOOSE  's' for seconds\n  ⁂  ")
            print(" ")
            print(" ")
            if y == "m":
                print("VALUE IN MINUTE IS :- ", n * 60, "minutes")
            elif y == "d":
                print("VALUE IN DAY IS :- ", n * 0.04166667, "days")
            elif y == "w":
                print("VALUE IN WEEK IS :- ", n * 0.005952381, "weeks")
            elif y == "mo":
                print("VALUE IN MONTH IS :- ", n * 0.001368925, "months")
            elif y == "s":
                print("VALUE IN SECOND IS :- ", n * 3600, "seconds")
            else:
                pass
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
    elif y.lower() == "area":  # Making it case-insensitive
        for _ in range(q):
            n = int(input("Enter Number To Be converted {IN ACRES } :- "))
            print(" ")
            y = input("                                      CHOOSE  'sqf' for square feet\n                                      CHOOSE  'h' for hectare\n                                      CHOOSE  'sqg' for square gaj\n                                      CHOOSE  'b' for bigha\n                                      CHOOSE  'sqk' for square kilometer\n  ⁂  ")
            print(" ")
            print(" ")
            if y == "sqf":
                print("VALUE IN SQUARE FEETS IS :- ", n * 43560.00001, "squarefeets")
            elif y == "h":
                print("VALUE IN HECTARE IS :- ", n * 0.4046856422, "hectares")
            elif y == "sqg":
                print("VALUE IN SQUARE GAJ IS :- ", n * 4840.040281, "sq. gajs")
            elif y == "b":
                print("VALUE IN BIGHAS IS :- ", n * 1.6, "bighas")
            elif y == "sqk":
                print("VALUE IN SQUARE KILOMETER IS :- ", n * 0.004046856422, "sq.kilometers")
            else:
                pass
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
    elif y.lower() == "money":  # Fixing typo and making it case-insensitive
        for _ in range(q):
            n = int(input("Enter Number To Be converted {IN INR } :- "))
            print(" ")
            y = input("                                      CHOOSE  'usd' for for us dollar \n                                      CHOOSE  'eu' for euro\n                                      CHOOSE  'yen' for japanese yen \n                                      CHOOSE  'peso' for philippine \n                                      CHOOSE  'won' for south korean won \n  ⁂  ")
            print(" ")
            print(" ")
            if y == "usd":
                print("VALUE IN US DOLLAR IS :- ", n * 0.011993, "$")
            elif y == "eu":
                print("VALUE IN EURO IS :- ", n * 0.011035, "€")
            elif y == "yen":
                print("VALUE IN JAPANESE YEN IS :- ", n * 1.759766, "¥")
            elif y == "peso":
                print("VALUE IN PHILIPPINES IS :- ", n * 0.663507, "₱")
            elif y == "won":
                print("VALUE IN SOUTH KOREAN WON IS :- ", n * 3600, "₩")
            # ELSE will pass the command if it's wrong or no value is entered
            else:
                pass
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
    else:                          
        break  # Exit the loop if the user enters an invalid input

input("PRESS ANY KEY TO EXIT        ")
