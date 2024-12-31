import time
import random
import os
colors = ["\033[32m", "\033[90m", "\033[34m"]
reset_color = "\033[0m"

def intro():
    textf = "HackerSim 2024..."
    text = ""
    text2f = "The sequel that no one asked for"
    text2 = ""
    try:
        columns, rows = os.get_terminal_size()
    except OSError as e:
        print("OSError: not supported defaulting to default")
        columns = 50
        rows = 30
    for frame in range(60):
        buffer = ""
        textind = 0
        textind2 = 0
        for y in range(rows):
            for x in range(columns):
                # Center of the screen
                if y == round(rows / 2) and (columns // 2 - len(text) // 2 <= x < columns // 2 + len(text) // 2):
                    buffer += text[textind]
                    textind += 1
                elif y == round(rows / 2) + 1 and (columns // 2 - len(text2) // 2 <= x < columns // 2 + len(text2) // 2):
                    buffer += text2[textind2]
                    textind2 += 1
                else:
                    buffer += colors[random.randint(0, 2)] + chr(random.randint(32, 126)) + reset_color
        print(buffer)
        if frame>=5 and len(text)<(frame-5):
            text+=textf[frame-5]
        if frame>=25 and len(text2)<(frame-25):
            text2+=text2f[frame-25]
        time.sleep(0.1)
