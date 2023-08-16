'''
This file contains the player class.
'''
INITIAL = 100

class Player():
    '''
    The class for players. 
    Holds the players current list of cards.
    '''

    def __init__(self):
        self.hand = []
        self.score = 0


    def add_card(self, card):
        '''
        This function allows players to add a card object to their hand. 
        '''
        self.hand.append(card)
        

    def calculate_score(self):
        self.score = 0
        num_aces = 0
        
        for card in self.hand:
            rank = card.rank
            if rank == "A":
                num_aces += 1
            elif rank in ["K", "Q", "J"]:
                self.score += 10
            else:
                self.score += int(rank)

        # Add aces based on best possible value
        for _ in range(num_aces):
            if self.score + 11 <= 21:
                self.score += 11
            else:
                self.score += 1
        
        return self.score
