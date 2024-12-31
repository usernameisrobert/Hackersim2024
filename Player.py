from typing import Optional, Callable

class Item:
    name: str
    short_description: str
    uses: int = -1  # a negative number means unbreakable
    on_use: Optional[Callable] = None
    destroyed: bool = False

    def __init__(self, name: str, description: str, uses: int = -1):
        self.name = name
        self.short_description = description
        self.uses = uses

    def __str__(self) -> str:
        return f'{self.name}: {self.short_description}'

    def add_onuse(self, func: Callable):
        self.on_use = func

    def use(self, player) -> bool:
        """Should return false if the item been destroyed"""
        if self.destroyed:
            return False
        if self.on_use:
            self.on_use(self, player)
        if self.uses >= 0:
            self.uses -= 1
            if self.uses <= 0:
                self.destroyed = True
        return True

# I did not write this, some ai did and he did amazing :)
class Inventory:
    items: list[Item]
    slots: int

    def __init__(self, start_items: Optional[list[Item]] = None, slots: int = 12):
        self.items = start_items if start_items is not None else []
        self.slots = slots

    def add_item(self, item: Item) -> bool:
        """Add an item to the inventory if there is space."""
        if len(self.items) < self.slots:
            self.items.append(item)
            return True
        return False

    def get(self, index: int) -> Item:
        return self.items[index]

    def __index__(self, i) -> Item:
        return self.get(i)


    def remove_item(self, item: Item) -> bool:
        """Remove an item from the inventory."""
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    def is_full(self) -> bool:
        """Check if the inventory is full."""
        return len(self.items) >= self.slots

class Player:
    health: float
    money: float
    repuation: int
    suspison: int

    def __init__(self, money: float = 20):
        self.health = 100
        self.money = money
        self.repuation = 0
        self.suspison = 0