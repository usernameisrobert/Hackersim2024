import typing

from Player import Player
from typing import Callable

class Path:
    def __init__(self, description, paths, on_call: Callable[[Player, list, int | None], int], auto_input: bool = True):
        self.description = description
        self.paths = paths
        self.on_call = on_call
        self.auto_input = auto_input

    @staticmethod
    def get_input(prompt='> ') -> int:
        while True:
            try:
                return int(input(prompt))
            except Exception:
                print("Must enter a number")

    def enter(self, player: Player) -> typing.Optional:
        print(self.description)
        val: int | None = self.get_input() if self.auto_input else None
        index = self.on_call(player, self.paths, val)
        if index == -1 or not self.paths:
            return None
        return self.paths[index]

class Ending(Path):
    @staticmethod
    def enter_end(player: Player, paths, index) -> int:
        return -1

    def __init__(self, description):
        super().__init__(description, None, on_call=self.enter_end, auto_input=False)