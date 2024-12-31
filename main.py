import time
import random
import os

colors = ["\033[32m","\033[90m","\033[34m"]

name = input("name: ")

print(f"YOU ARE {name}\nhealth: 100\nmoney: 20\ncan you guess a number between 1 and 5")

number = random.randint(1, 5)

guess = 0

while guess != number:
    try:
        guess = int(input("guess: "))
    except:
        pass

text=""

for frame in range(30):
    rows, columns = os.get_terminal_size()
    for y in range(columns):
        for x in range(rows):
            if (y == round(rows/2)) and ():
                
            print(colors[random.randint(0,2)] + chr(random.randint(32, 126)), end='')
        print()
    time.sleep(0.1)