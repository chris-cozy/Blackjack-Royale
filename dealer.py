'''
This file contains the dealer class.
'''

class Dealer():
    '''
    The class for dealers. 
    Holds the dealers current list of cards.
    '''

    def __init__(self):
        self.name = 'Dealer'
        self.all_cards = []


    def add_cards(self, cards):
        '''
        This function allows dealers to add cards to their hand. 
        It can be either a single card object or a list of card objects
        '''
        if type(cards) == type([]):
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)
        

    def __str__(self):
        return f"{self.name}"