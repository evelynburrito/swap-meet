from .item import Item

class Electronics(Item):
    category = "Electronics"

    def __init__(self, condition = 0):
        self.condition = condition

    def __str__(self):
        return "A gadget full of buttons and secrets."
