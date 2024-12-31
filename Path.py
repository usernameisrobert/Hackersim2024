class Path:
    def __init__(self, description, connected, on_call):
        self.description = description
        self.connected = connected
        self.on_call = on_call

    def enter(self, player):
        pass