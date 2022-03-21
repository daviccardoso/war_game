from random import shuffle
from card import Card
from global_objects import suits, ranks


class Deck:
    """Deck class"""

    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        """Shuffle the deck"""
        shuffle(self.all_cards)

    def deal_one(self):
        """Remove card from the deck"""
        return self.all_cards.pop()

    def __len__(self):
        return len(self.all_cards)
