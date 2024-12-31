import time
import random
import os
import platform
from Player import Player
from intro import intro

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def main():
    name = input("name: ")

    player = Player(name)
    print(player)
    print("Can you guess the number between 1 and 5?")

    number = random.randint(1, 5)
    guess = 0
    while guess != number:
        try:
            guess = int(input("guess: "))
        except Exception:
            print("You must enter a number")

    intro()
    clear()
    print("The end")

if __name__ == "__main__":
    main()
