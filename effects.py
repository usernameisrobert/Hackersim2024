import random
import time

def get_index(text_list) -> int:
    while True:
        index = random.randint(0, len(text_list) - 1)  # Pick a random index
        if text_list[index] not in [' ', '\t', '\n']:
            return index

def rand_char(text) -> str:
    text_list = list(text)
    index = get_index(text_list)

    if random.random() < 0.8:
        # 80% chance to change the character to a random printable character
        text_list[index] = chr(random.randint(32, 126))
    else:
        # 20% chance to change the character to a space
        text_list[index] = ' '

    return ''.join(text_list)

def remove(text) -> str:
    text_list = list(text)
    index = get_index(text_list)

    text_list[index] = ' '
    return ''.join(text_list)

def evaporate(text: str):
    """prints the text to the screen and evaps it"""
    cursor_to_begin_nclear = "\33[2K\r" # Some ansi magic ;)
    tmp_text = text
    for frame in range(10):
        tmp_text = rand_char(tmp_text)
        time.sleep(0.1) # If you don't know what this is your dumb

        print(cursor_to_begin_nclear + tmp_text, end='')
        if not tmp_text.strip(' '):
            return

    # whoever sees this, you gay...
    while True:
        tmp_text = remove(tmp_text)
        time.sleep(0.1)
        print(cursor_to_begin_nclear + tmp_text, end='')
        if not tmp_text.strip(' '):
            return