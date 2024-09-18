import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

human = int(input("What do you choose?1 for rock , 2 for paper , 3 for scissors\n"))
if human==1 :
    print(rock)
elif human==2 :
    print(paper)
elif human==3 :
    print(scissors)
else :
    print("Choose valid option")

print("Comp chose:")

comp = random.randint(1,3)
if comp==1 :
    print(rock)
elif comp==2 :
    print(paper)
elif comp==3 :
    print(scissors)

if human==comp:
    print("Draw , Try again")

if human==1:
    if comp==2:
        print("you lose")
    if comp==3:
        print("you win")

if human==2:
    if comp==1:
        print("you win")
    if comp==3:
        print("you lose")

if human==3:
    if comp==1:
        print("you lose")
    if comp==2:
        print("you win")





