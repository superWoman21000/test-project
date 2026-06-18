"""Simple in-memory inventory manager."""


class Inventory:
    """Tracks item quantities in a small warehouse system."""

    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        """Add quantity of an item to the inventory."""
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
        return self.items[name]

    def remove_item(self, name, quantity):
        """Remove quantity of an item from the inventory."""
        if name not in self.items:
            raise KeyError(f"Item '{name}' not found")
        if self.items[name] < quantity:
            raise ValueError("Not enough stock to remove")
        self.items[name] -= quantity
        return self.items[name]

    def get_quantity(self, name):
        """Return the current quantity for an item, or 0 if absent."""
        return self.items.get(name, 0)
