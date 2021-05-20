#Name: Leon Chen
#Date: April 30
#this program displays a favourite colour along with a favourite food

#input data
colour=str(input("Enter your favourite colour:"))
food=str(input("Enter your favourite food:"))

#process data
if colour==("blue"):
    if food==("sushi"):
        print("My favourite colour is blue and my favourite food is sushi.")
else:
    if colour==("blue"):
        if food==("soup"):
            print("My favourite colour is blue ad my favourite food is soup.")
    else:
        if colour==("blue"):
            if food!=("soup"):
                print("My favourite colour is blue.")
        else:
            if colour==("blue"):
                if food!=("sushi"):
                    print("My favourite colour is blue.")
            else:
                if colour==("red"):
                    if food==("pizza"):
                        print("My favourite colour is red and my fvaourite food is pizza.")
                else:
                    if colour==("red"):
                        if food!=("pizza"):
                            print("My favourite colour is red.")
                    else:
                        if colour!=("red"):
                            print("My favourite colour is " +colour)
                        else:
                            if colour!=("blue"):
                                print("My favourite colour is " +colour)
                
