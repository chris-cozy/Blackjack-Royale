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
        self.value = 0


    def add_card(self, card):
        '''
        This function allows the dealer to add a card object to their hand. 
        '''
        if card.value == 11:
            self.ace(card)
        self.all_cards.append(card)
        self.value += card.value

    def ace(self, card):
        if self.value + 11 <= 21:
            pass
        else :
            card.value = 1
        

    def __str__(self):
        return f"{self.name}"