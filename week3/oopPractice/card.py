
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        try:
            value = int(value)
        except ValueError:
            raise AttributeError("Value is not a string")
        if value <= 0 or value >= 10:
            raise AttributeError("Value is invalid")
        if color != ("red" or "RED") and color != ("black" or "BLACK"):
            raise AttributeError("Color is invalid")
        pass
    
    def is_stronger_than(self, other_card):
        self.other_card = other_card
        return self.value >= other_card.value


five_black = Card(5, "black")
ten_red = Card(10, "red")
ten_red.is_stronger_than(five_black)