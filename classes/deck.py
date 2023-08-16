'''
The deck class.
'''
import random
from classes.card import Card, RANKS, SUITS

class Deck:
    '''
    The deck class. It instantiates a new deck, creating all 52 card objects and keeping them in a list.
    It can shuffle the deck, as well as deal cards from it.
    '''
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS ]

    def shuffle(self):
        '''
        This will shuffle the deck of cards. Uses the random library
        '''
        random.shuffle(self.cards)

    def deal(self):
        '''
        This returns a card from the top of the stack, then removes it from the list.
        '''
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            print("The deck is empty!")

    def __str__(self):
        for card in self.cards:
            print(card)