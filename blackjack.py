'''
This file contains the blackjack game loop.
'''
import dealer
import deck
import player
import random

GOAL = 21
BAR = "//-------------------------------------//"

def hidden_display(player, dealer):
    print(BAR)
    print(f"{player.name} cards: ")
    print('', *player.all_cards, sep = '\n')
    print(f"Value: {player.value}")
    print(BAR)
    print(f"{dealer.name} cards: ")
    print("< hidden card >")
    print('', dealer.all_cards[1], sep = '\n')
    print(f"Value: ???")
    print(BAR)

def full_display(player, dealer):
    print(BAR)
    print(f"{player.name} cards: ")
    print('', *player.all_cards, sep = '\n')
    print(f"Value: {player.value}")
    print(BAR)
    print(f"{dealer.name} cards: ")
    print('', *dealer.all_cards, sep = '\n')
    print(f"Value: {dealer.value}")
    print(BAR)

def display(player):
    print(BAR)
    print(f"{player.name} cards: ")
    print('', *player.all_cards, sep = '\n')
    print(f"Value: {player.value}")
    print(BAR)

def check_for_win(dealer, player, bet):
    if player.value > GOAL:
        print(f"{player.name} HAS BUSTED! Round over!")
        print(f"{player.name} has lost {bet} chips!")
        player.bankroll -= bet
        return True
    elif dealer.value > GOAL:
        print(f"{dealer.name} HAS BUSTED! ROUND OVER!")
        print(f"{player.name} has won {bet * 2} chips!")
        player.bankroll += (bet * 2)
        print(BAR)
        return True
    elif dealer.value > player.value:
        print(f"{dealer.name} WINS THE ROUND!")
        print(f"{player.name} has lost {bet} chips!")
        player.bankroll -= bet
        print(BAR)
        return True
    else:
        return False

def first_deal(player, dealer, deck):
    for num in range(2):
        card = deck.deal()
        player.add_card(card)
        card = deck.deal()
        dealer.add_card(card)


if __name__ == '__main__':
    '''
    Game Logic
        Create players and deck
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
        p1.value = 0
        d1.value = 0

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
            first_deal(p1, d1, game_deck)
            hidden_display(p1, d1)

            #Player Turn
            player_turn = True
            print(f"{p1.name}'s turn.")
            while player_turn:
                if p1.value > GOAL:
                    check_for_win(d1, p1, bet)
                    player_turn = False
                    in_round = False
                else:
                    choice = int(input('Select an action:\n1. Hit\n2. Stay\nChoice: '))
                    if choice == 1:
                        new_card = game_deck.deal()
                        p1.add_card(new_card)
                        display(p1)
                    elif choice == 2:
                        player_turn = False

            #Dealer Turn
            dealer_turn = False
            if in_round:
                dealer_turn = True
                print(BAR)
                print(f"{d1.name}'s turn.")

            while dealer_turn:
                if check_for_win(d1,p1, bet):
                    dealer_turn = False
                    in_round = False
                elif d1.value <= p1.value:
                    print(f"{d1.name} hits.")
                    new_card = game_deck.deal()
                    d1.add_card(new_card)
                    display(d1)
        
        choice = int(input('Would you like to play another round?\n1. Yes\n2. No\nChoice: '))
        if choice == 1:
            in_round = True
            print(BAR)
            continue
        elif choice == 2:
            print('Thanks for playing.')
            game_on = False
  
      
