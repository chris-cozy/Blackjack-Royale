# blackjack


## Gamplay Loop
For this version of the game, there will be a human player and a computer dealer. We will start with a normal deck of cards. 
The player has a bankroll and can place a bet. The player starts with two cards face up, and the dealer starts with 1 card face up and one card face down. 
The player goes first. The player's goal is to get closer to a total value of 21 than the dealer does. The total value is the sum of the current face of cards.
Possible actions:
    - Hit (recieve another card)
    - Stay (stop receiving cards)
In this implementation, actions like insurance, split, or double down are not considered.
After the player's turn, if the player is under 21, the dealer will hit until they either beat the player of the dealer busts (goes over 21).

## Ending the game
If the player keeps hitting and goes over 21, they bust and lose the bet. In this case, the game is over and the dealer collects the money.
If the dealer sum is higher than the player's and still under 21, then the dealer wins.
If the dealer busts, the bet is doubled and given to the player, adding to their bankroll.

## Special Rules
Face cards (Jack, Queen, King) count as a value of 10.
Aces can count as either 1 or 11, whichever value is prefereable to the player.