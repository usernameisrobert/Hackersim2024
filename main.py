import time
import random
import os
import platform

colors = ["\033[32m","\033[90m","\033[34m"]
reset = "\033[0m"



text=""

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def intro_scene():
    clear()
    buf = ''
    rows, cols = os.get_terminal_size()
    CHAR_SIZE = 5 # 4 for ansi color 1 for character
    while True:
        for y in range(0, cols):
            for x in range(0, rows):
                color = colors[random.randint(0,len(colors)-1)]
                character = chr(random.randint(32, 126))
                buf += color + character
            buf += '\n'
        print(buf)
        time.sleep(0.1)

    # now we need to print the text centered of screen

def main():
    name = input("name: ")

    print(f"YOU ARE {name}\nhealth: 100\nmoney: 20\ncan you guess a number between 1 and 5")

    number = random.randint(1, 5)
    guess = 0
    while guess != number:
        try:
            guess = int(input("guess: "))
        except Exception:
            print("You must enter a number")

    intro_scene()

if __name__ == "__main__":
    main()
