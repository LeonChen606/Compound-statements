#Name: Leon Chen
#Date: April 22
#this program calculates the price of eggs

#input data
eggsDozen=int(input("Enter the amount of eggs in dozens:"))

#process data
if eggsDozen>=11:
    price=eggsDozen*6
    print("\nThe cost is $%.2f"% price)
elif eggsDozen>=6:
    price=eggsDozen*6.15
    print("\nThe cost is $%.2f"% price)
elif eggsDozen>=4:
    price=eggsDozen*6.25
    print("\nThe cost is $%.2f"% price)
else:
    price=eggsDozen*6.5
    print("\nThe cost is $%.2f"% price)
    
