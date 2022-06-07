'''
This file contains the deck class.
'''
import random
import card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Deck():
    '''
    The deck class. It instantiates a new deck, creating all 52 card objects and keeping them in a list.
    It can shuffle the deck, as well as deal cards from it.
    '''
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                new_card = card.Card(suit, rank)
                self.all_cards.append(new_card)

    def shuffle(self):
        '''
        This will shuffle the deck of cards. Uses the random library
        '''
        random.shuffle(self.all_cards)
        print("The deck has been shuffled.")

    def deal(self):
        '''
        This returns a card from the top of the stack, then removes it from the list.
        '''
        if len(self.all_cards) > 0:
            return self.all_cards.pop()
        else:
            print("The deck is empty!")