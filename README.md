# blackjack
This is a simple implementation of a console-based Blackjack game for two players using Python. The game allows two players to take turns dealing cards and deciding whether to continue or wait. The goal is to achieve a hand value as close to 21 as possible without exceeding it.

Features
Deck Creation: A standard deck of 52 cards is created and shuffled.
Card Values: Cards are assigned values based on Blackjack rules (Aces can be worth 1 or 11, face cards are worth 10).
Player Actions: Players can choose to deal a card or wait.
Turn Management: Players alternate turns, and the game continues until both players choose to wait or one player busts.
Win Conditions: The game checks for win conditions based on hand values and announces the winner or a tie.

How to Run
Clone the Repository: Clone this repository to your local machine using git clone https://github.com/yourusername/blackjack-game.git.
Run the Game: Execute the script using Python 3 by running python blackjack_game.py from your command line.

Game Flow
Initialization: Two empty hands for the players and a shuffled deck are prepared.

Gameplay Loop: Players take turns dealing cards or waiting. The game checks for win conditions after each turn.

End of Game: The game ends when both players have waited or a player busts, and the result is displayed.

Example
---- 
ROUND: 0 
PLAYER 1's TURN 
HAND 1: 10 8    TOTAL: 18 
What would you like to do? 
1) Deal            2) Wait 

Note: This game requires a terminal that supports ANSI escape codes for color output and screen clearing.

