#random num gen
from random import randrange
#loop value and random num 
x=1
numr1=randrange(0,100)
#loop
while x==1:
    #user input 
    input1=int(input("\nGuess the random number(0-100): "))
    #boolean
    if input1<numr1:
        print("Less than (Go higher)")
    elif input1>numr1:
        print("Greater than (Go lower)")

    if input1==numr1:
        print("You guessed the number!")
        x=0

    