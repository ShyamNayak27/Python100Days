import random
print("Number Guessing Game")
print("Number is between 1 and 100")
x= random.randrange(0,100)
def guess():
    global x
    dif = input("Choose a difficulty : Easy or Hard ").lower()
    if dif=="easy":
        for i in range(-10,0):
            print(f'You have {abs(i)} attempts remaining to guess')
            tryy=int(input("Make a guess "))
            if tryy<x:
                print("too low")
            elif tryy>x:
                print("Too high")
            else:
                print("You won")
                break
        if tryy==x:
            pass
        else:
            print("You ran out of guesses,You lose")

    else:
        for i in range(-5,0):
            print(f'You have {abs(i)} attempts remaining to guess ')
            tryy=int(input("Make a guess "))
            if tryy<x:
                print("too low")
            elif tryy>x:
                print("Too high")
            else:
                print("You won")
                break
        if tryy==x:
            pass
        else:
            print("You ran out of guesses,You lose")

guess()
