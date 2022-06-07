'''
This file contains the player class.
'''
init_bank = 100

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
        self.bankroll = init_bank


    def add_cards(self, cards):
        '''
        This function allows players to add cards to their hand. 
        It can be either a single card object or a list of card objects
        '''
        if type(cards) == type([]):
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)
        

    def __str__(self):
        return f"Player {self.name} has a bankroll of ${self.bankroll}"
