#Name: Leon Chen
#Date: April 22
#this program prints a message depending on your age

#input data
age=int(input("Enter your age:"))

#process data
if age>18:
    print("\nAdult.")
elif age>12:
    print("\nTeen.")
elif age>10:
    print("\nPreteen.")
elif age>5:
    print("\nChild.")
else:
    print("\nToddler.")
