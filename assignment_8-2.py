from random import randrange

x=1
numr1=randrange(0,100)

input1=int(input("Guess the random number: "))

while x==1:
    if input1<numr1:
        print("Lower than")
    elif input1>numr1:
        print("Greater than")