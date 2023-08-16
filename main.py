'''
This file contains the blackjack game loop.
'''
from classes.card import Card
from classes.deck import Deck
from classes.player import Player
import random

def display_hands(player, dealer, show_dealer_hand=True):
    print("Player's Hand:", [str(card) for card in player.hand])
    if show_dealer_hand:
        print("Dealer's Hand:", [str(card) for card in dealer.hand])
    else:
        print("Dealer's Hand:", [str(dealer.hand[0]), "Hidden"])

def display_scores(player, dealer, show_dealer_score=True):
    print("Player's Score:", player.calculate_score())
    if show_dealer_score:
        print("Dealer's Score:", dealer.calculate_score())

def display_game_status(result):
    print("Game Result:", result)

def player_turn(player, deck):
    while True:
        display_hands(player, dealer, show_dealer_hand=False)
        display_scores(player, dealer, show_dealer_score=False)

        decision = input("Do you want to hit or stand? (h/s): ")

        if decision.lower() == "h":
            player.add_card(deck.deal())
            if player.calculate_score() > 21:
                display_hands(player, dealer)
                display_scores(player, dealer)
                print("Bust! You lose.")
                return "lose"
        else:
            return "stand"

def dealer_turn(dealer, deck):
    while True:
        display_hands(player, dealer, show_dealer_hand=True)
        display_scores(player, dealer)

        while dealer.calculate_score() < 17:
            dealer.add_card(deck.deal())

        return

def determine_game_result(player, dealer):
    player_score = player.calculate_score()
    dealer_score = dealer.calculate_score()

    if player_score > 21:
        return "Dealer wins!"
    elif dealer_score > 21:
        return "Player wins!"
    elif player_score > dealer_score:
        return "Player wins!"
    elif dealer_score > player_score:
        return "Dealer wins!"
    else:
        return "It's a draw!"
    

if __name__ == '__main__':
    '''
    Main game logic
    '''
    # Initialize the deck and players
    deck = Deck()
    deck.shuffle()

    player = Player()
    dealer = Player()

    # Deal cards to players
    for _ in range(2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
    
    result = player_turn(player, deck)
    if result == "lose":
        print("Dealer wins!")
        exit()
    else:
        dealer_turn(dealer, deck)

    display_hands(player, dealer, show_dealer_hand=True)
    display_scores(player, dealer)

    game_result = determine_game_result(player, dealer)
    print(game_result)