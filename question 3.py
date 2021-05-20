#Name: Leon Chen
#Date: April 30
#this program determines a grade depending on the mark given

#input data
mark=float(input("Enter your mark:"))

#process data
if mark>100:
    print("Not a real grade.")
else:
    if mark<0:
        print("Not a real grade.")
    else:
        if mark<50:
            print("F")
        else:
            if mark<60:
                print("C")
            else:
                if mark<80:
                    print("B")
                else:
                    if mark<90:
                        print("A")
                    else:
                        print("A+")
