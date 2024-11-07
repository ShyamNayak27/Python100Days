import random
from random import choice

import game_data
from game_data import data\

import art
from art import vs
from art import logo

def game():

    a = (random.choice(data))
    y = a["name"] + " , a " + a["description"] + " , from " + a["country"]
    i = 0
    repo=True

    while repo:

        b = (random.choice(data))
        z = b["name"] + " , a " + b["description"] + " , from " + b["country"]

        print(logo)
        print("Compare A: " + y)
        print(vs)
        print("Compare B: " + z)

        choice = input("Choose A or B?").lower()
        winner = ""
        if a["follower_count"]>b["follower_count"]:
            winner = "a"
        else:
            winner = "b"

        if choice!=winner:
            # print(choice)
            # print(winner)
            print(f'Wrong Answer, You lose , Final score={i}')
            break
        else:
            y=z
            i+=1
            print(f'Score is {i}')
            print("\n"*20)

game()