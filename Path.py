from Player import Player
class Path:
    def __init__(self, description, paths, on_call, auto_input: bool = True):
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

    def enter(self, player: Player):
        print(self.description)
        val: int | None = self.get_input() if self.auto_input else None
        self.on_call(player, self.paths, val)
