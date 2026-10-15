import random
#Number Guessing Game	Loops, Conditions, Random
n=random.randint(1,100)
a=int(input("Guesses the Number: "))
guesses=1
while(a!=n and guesses<7):
    
    if(a>n):
        print("Lower number place: ")
        a=int(input("Guesses the Number: "))
        guesses+=1
    else:
        print("Higher Number place: ")
        a=int(input("Guesses the Number: "))
        guesses+=1


if(a==n):
    print(f"You have guess the number: {n} Correctly in {guesses} attempt")
else:
    print("Game Over!")
    print("The correct number was {n}")
