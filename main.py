import time
import random
import os
import platform

colors = ["\033[32m","\033[90m","\033[34m"]
reset = "\033[0m"

text="HACKERSIM 2024"

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def intro_scene():
    clear()
    path = f"scripts/{platform.system()}/Intro"
    # we want to run this file as a executable and wait for it to finish
    os.system(path)

def main():
    name = input("name: ")

    print(f"YOU ARE {name}\nHealth: 100\nMoney: 20\nCan you guess a number between 1 and 5?")

    number = random.randint(1, 5)
    guess = 0
    while guess != number:
        try:
            guess = int(input("guess: "))
        except Exception:
            print("You must enter a number")

    intro_scene()
    clear()
    print("The end")

if __name__ == "__main__":
    main()
