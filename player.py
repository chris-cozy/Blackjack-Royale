'''
This file contains the player class.
'''
INITIAL = 100

class Player():
    '''
    The class for players. 
    Holds the players current list of cards.
    Holds the player's bankroll.
    A player is given an action choice.
    A player is able to hit.
    A player is able to stay
    '''

    def __init__(self, name):
        self.name = name
        self.all_cards = []
        self.bankroll = INITIAL
        self.value = 0


    def add_card(self, card):
        '''
        This function allows players to add a card object to their hand. 
        '''
        if card.value == 11:
            self.ace(card)
        self.all_cards.append(card)
        self.value += card.value

    def ace(self, card):
        choice = int(input("Choose a value for the Ace card:\n1. 1\n2. 11\nChoice: "))
        if choice == 1:
            card.value = 1
        else:
            pass
        

    def __str__(self):
        return f"Player {self.name} has a bankroll of ${self.bankroll}"
