from Path import Path, Ending
from Player import Player
import time

def root_fn(player: Player, paths: list[Path], option: int | None) -> int:
    if option is None:
        raise Exception("Option must not me None")

    #TODO: add more stats based on option
    return option


root = Path("""
There has been a murder in the area, but you have no idea who or what killed them.
You can go for a quick buck and break into the fbi data base and sell the information
or you can try and find the murderer and posibly get money for it but may be hard.
1) Sell Info (+3r +5s +$100)
2) Find Murderer (+3r -3s -/+$250)
3) ignore... (+0)
""", paths=[
    None,
    None,
    Ending("You ignored the murderer...\nlater that day you gotten a kncoked and before you could say anthing you gotten stabbed...\n"
           "KILLED BY THE MURDER ENDING")
], on_call=root_fn)

def start(player: Player):
    root.enter(player)