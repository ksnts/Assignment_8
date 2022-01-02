from random import randrange

x=1
numr1=randrange(0,100)

while x==1:
    input1=int(input("Guess the random number: "))
    if input1<numr1:
        print("Lower than")
    elif input1>numr1:
        print("Greater than")

    if input1==numr1:
        print("You guessed the number!")
        x=0

    