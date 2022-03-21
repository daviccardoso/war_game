from global_objects import values


class Card:
    """Card class"""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __len__(self):
        return self.value
