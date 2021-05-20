#Name: Leon Chen
#Date: April 30
#this program tells you whether you should work and where you should work

#input data
age=int(input("Enter your age:"))

#process data
if age<18:
    print("You are not eligible to work!")
else:
    if age<=40:
        print("You are eligible for outdoor work!")
    else:
        if age<=60:
            print("You are eligible for indoor work!")
        else:
            print("Not allowed to work as per government rules.")
