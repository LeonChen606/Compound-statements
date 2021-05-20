#Name: Leon Chen
#Date: April 22
#this program determines the amount of roots in a discriminant

#input data
number1=float(input("Enter a value for a:"))
number2=float(input("Enter a value for b:"))
number3=float(input("Enter a value for c:"))

#process data
if number2**2-4*number1*number3<0:
    print("\nNo roots.")
elif number2**2-4*number1*number3>0:
    print("\nTwo roots.")
else:
    print("\nOne root.")
