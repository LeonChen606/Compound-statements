#Name: Leon Chen
#Date: April 22
#This program displays a message depending on the height of the waves

#input data
waves=float(input("Enter the height of the waves in feet:"))

#process data
if waves>=6:
    print("\nGreat surfing day!")
elif waves>=3:
    print("\nGo body boarding!")
elif waves>0:
    print("\nGo for a swim.")
else:
    print("\nWhoa! What kind of surfing is that?")
