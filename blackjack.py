'''
This file will contain the game loop.
What we need:
    - Card Object
    - Deck Object
    - Player Object
    - Dealer Object
Functions:
    - calculate the value of cards for a player
'''
import dealer
import deck
import player
import random

GOAL = 21
BAR = "//-------------------------------------//"

def val(list):
    '''
    This function calculates the total value of a player's cards
    '''
    value = 0
    for card in list:
        value += card.val()

    return value

def display(list):
    for card in list:
        print(card)


if __name__ == '__main__':
    '''
    Game Logic
        Create players
        Create and shuffle deck
        Begin game.
        At the beginning of each round, deal two cards to both players.
        While it is player one's turn, they can choose to hit or stay.
            If they bust, the round is over, they lose their bet
        While it is the dealer's turn (if player is under 21) the dealer hits until
        they get a value higher than the player and win, or until they bust.
            If they bust, the player wins and recieves double the bet
            If they win, the round is over and player loses bes
    '''

    p1 = player.Player('Turtle')
    d1 = dealer.Dealer()

    round_num = 0
    in_round = True

    game_on = True
    while game_on:

        del p1.all_cards[:]
        del d1.all_cards[:]

        game_deck = deck.Deck()
        game_deck.shuffle()

        
        round_num += 1
        while in_round:
            print(BAR)
            bet = int(input(f"How much do you want to bet?\nYour chips: {p1.bankroll}\nBet amount: "))
            while bet > p1.bankroll:
                print("You don't have enough chips, either bet smaller or stop playing...")
                bet = int(input(f"How much do you want to bet?\nYour funds: {p1.bankroll}\nBet amount: "))
            print(BAR)
            print(f"Dealing cards for Round {round_num}...")
            #Deal the starting cards
            for num in range(2):
                p1.all_cards.append(game_deck.deal())
                d1.all_cards.append(game_deck.deal()) 

            print(BAR)
            print(f"{p1.name} cards: ")
            display(p1.all_cards)
            print(f"Value: {val(p1.all_cards)}")
            print(BAR)
            print(f"{d1.name} cards: ")
            display(d1.all_cards)
            print(f"Value: {val(d1.all_cards)}")
            print(BAR)

            #Player Turn
            player_turn = True
            print(f"{p1.name}'s turn.")
            while player_turn:
                #Player lost
                if val(p1.all_cards) > GOAL:
                        print(f"{p1.name} HAS BUSTED! Round over!")
                        print(f"{p1.name} has lost {bet} chips!")
                        p1.bankroll -= bet
                        player_turn = False
                        in_round = False
                        break
                choice = int(input('Select an action:\n1. Hit\n2. Stay\nChoice: '))
                if choice == 1:
                    p1.all_cards.append(game_deck.deal())
                    print(BAR)
                    print(f"{p1.name} cards: ")
                    display(p1.all_cards)
                    print(f"Value: {val(p1.all_cards)}")
                    print(BAR)
                elif choice == 2:
                    player_turn = False

            #Dealer Turn
            dealer_turn = False
            if in_round:
                dealer_turn = True
                print(BAR)
                print(f"{d1.name}'s turn.")

            while dealer_turn:
                if val(d1.all_cards) > GOAL:
                    #Player has won
                    print(f"{d1.name} HAS BUSTED! ROUND OVER!")
                    print(f"{p1.name} has won {bet * 2} chips!")
                    p1.bankroll += (bet * 2)
                    print(BAR)
                    dealer_turn = False
                    in_round = False
                elif val(d1.all_cards) > val(p1.all_cards):
                    #Dealer has won
                    print(f"{d1.name} WINS THE ROUND!")
                    print(f"{p1.name} has lost {bet} chips!")
                    p1.bankroll -= bet
                    print(BAR)
                    dealer_turn = False
                    in_round = False
                elif val(d1.all_cards) <= val(p1.all_cards):
                    print(f"{d1.name} hits.")
                    d1.all_cards.append(game_deck.deal())
                    print(BAR)
                    print(f"{d1.name} cards: ")
                    display(d1.all_cards)
                    print(f"Value: {val(d1.all_cards)}")
                    print(BAR)
        
        choice = int(input('Would you like to play another round?\n1. Yes\n2. No\nChoice: '))
        if choice == 1:
            in_round = True
            print(BAR)
            continue
        elif choice == 2:
            print('Thanks for playing.')
            game_on = False
            break
  
      
