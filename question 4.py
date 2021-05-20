#Name: Leon Chen
#Date: April 30
#this program determines what season the person was born in

#input data
month=int(input("Enter the month you were born as a numerical value:"))

#process data
if month<=2:
    print("Winter.")
else:
    if month<=5:
        print("Sping.")
    else:
        if month<=8:
            print("Summer.")
        else:
            if month<=11:
                print("Fall.")
            else:
                if month==12:
                    print("Winter.")
                else:
                    print("not a valid month.")
