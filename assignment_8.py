#random num gen
from random import randrange
#x is for the loop value
x=1
#while loop for continuous play
while x == 1:
#random numbers from 0-9
    numr1=randrange(0,9)
    numr2=randrange(0,9)
    numr3=randrange(0,9)
#user input
    num1=int(input("Enter first number(0-9): "))
    num2=int(input("Enter second number(0-9): "))
    num3=int(input("Enter third number(0-9): "))
#list for the lotto numbers
    lottoN= [numr1, numr2, numr3]
    lottoU= [num1, num2, num3]
#output
    print(f"Lotto Numbers are: {lottoN}")
#win/lose if else
    if lottoN == lottoU:
        print("WINNER!!!")
    else:
        print("You lost!")
#boolean for looping
    print("Try again? y/n")
    loop1=str(input(": "))

    if loop1.lower() == "n":
        x=0
        print("Thank you!")
    elif loop1.lower() == "y":
        x=1
    else:
        print("Invalid input!\nCode will now terminate.")
        x=0





    







