#Name: Leon Chen
#Date: April 30
#this program determines the price to print copies

#input data
copies=int(input("Enter the amount of copies needed:"))

#process data
if copies<100:
    price=0.3
else:
    if copies<500:
        price=0.28
    else:
        if copies<750:
            price=0.27
        else:
            if copies<1000:
                price=0.26
            else:
                price=0.25
total=price*copies

#output data
print("\nThe total cost will be $%.2f at $%.2f per copy."%(total, price))
