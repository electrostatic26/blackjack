import random
import os
import time
import sys
def create_deck():
    '''
    Creates the the deck 
    '''
    # Create a list of card values from A to K, repeating 4 times each
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
    # Shuffle the deck to randomize the order
    random.shuffle(values)
    return values

def card_value(card):
    '''
    Creates a dictionary to map each "character" to a numerical value
    Example to access a value in a dict from key
    a Key: 'A'
    a Value: 11

    print(card_values['A']) -> 11
    '''
    # Dictionary to map card values to their corresponding integer values
    card_values = {
        'A': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }
    # Check if the card is valid and return its value
    if card in card_values:
        return card_values[card]
    else:
        print("Error: Invalid card")
        return 0

def get_value(hand):
    '''
    sums up the value of the users cards
    '''
    # Calculate the sum of the card values in the hand
    value = sum(card_value(card) for card in hand)
    # Count the number of aces in the hand
    aces = hand.count('A')


    # Adjust the value if the hand contains aces and the total value exceeds 21
    # if the hand is over 21 and has aces, then we change the value of aces to 1

    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def print_hand(num, hand):
    '''
    Prints the users hand
    '''
    # Call the "get_value" function to determine the value of the hand
    value = get_value(hand)

    # Convert the list of cards in the hand to a string with spaces in between each card
    hand_as_string = " ".join(hand)

    # Print out the player's hand and its total value
    # The "f" in front of the string allows us to include variables within the string
    print(f"HAND {num + 1}: {hand_as_string}    TOTAL: {value}")

def check_busted(hand):
    # Check if the total value of the hand exceeds 21
    return get_value(hand) > 21

def check_win(hand1, hand2, done1, done2):
    # Get the values of both hands
    value1 = get_value(hand1)
    value2 = get_value(hand2)
    
    # Check if any player has busted
    busted1 = check_busted(hand1)
    busted2 = check_busted(hand2)
    
    # Determine the game outcome
    if busted1 and busted2:
        return 2  # Both players lose
    elif busted1:
        return 1  # Player 1 loses
    elif busted2:
        return 0  # Player 2 loses
    
    if done1 and done2:
        # Both players have finished, determine the winner based on hand values
        if value1 > value2:
            return 0  # Player 1 wins
        elif value2 > value1:
            return 1  # Player 2 wins
        else:
            return 2  # Tie

    return -1  # Game is not yet decided

# THIS IS WHERE THE GAME REALLY STARTS
# initialize two empty lists to represent each player's hand
a = []  # player 1's hand
b = []  # player 2's hand

# create a deck of cards
deck = create_deck()

# initialize variables to track game state
round = 0  # current round number
turn = 0  # current player's turn

# keep track of whether each player has pressed "wait" in the current round
p1Done = False
p2Done = False

while True:
    game_end = False

    # check if both players have pressed "wait" in the current round
    if p1Done and p2Done:
        game_end = True
    # if it's player 1's turn and they've already pressed "wait", skip their turn
    elif turn == 0 and p1Done:
        turn = (turn + 1) % 2
        if turn == 0:
            round += 1
        continue
    # if it's player 2's turn and they've already pressed "wait", skip their turn
    elif turn == 1 and p2Done:
        turn = (turn + 1) % 2
        continue

    print("----")
    print(f"ROUND: {round}")
    print(f"PLAYER {turn + 1}'s TURN")

    # print the current player's hand
    if turn == 0:
        hand = a
    else:
        hand = b
    print_hand(turn, hand)

    # give the current player the option to deal a card or wait
    print()
    print("----")

    # ensure the user gives valid input using a while loop
    while True:
        print("What would you like to do?")
        print("1) Deal            2) Wait")

        command = input()
        if command == "1":

            for x in range(1,14):                
                os.system('cls')
                s1 = "Generating Card ["
                templ = ['>    ]','>>   ]','>>>  ]','>>>> ]','>>>>>]']
                print(f'\033[36m{s1}{templ[(x%5)-1]}\033[0m')
                #print(s1+templ[(x%5)-1])
                time.sleep(0.06)

            os.system('cls')
            if turn == 0:
                a.append(deck.pop())
                tempa = str(a[-1])
                print(f'\033[31mDEALED A [{tempa}] TO PLAYER 1\033[0m')
            else:
                b.append(deck.pop())
                tempb = str(b[-1])
                print(f'\033[31mDEALED A [{tempb}] TO PLAYER 1\033[0m')
            break
        elif command == "2":
            # record that the current player has chosen to wait in the current round
            os.system('cls')

            if turn == 0:
                p1Done = True
            else:
                p2Done = True
            break
        else:
            print("Invalid Command, Try Again")

    # check for a win after each player's turn
    win = check_win(a, b, p1Done, p2Done)
    if win != -1:
        print("GAME OVER")
        print("PLAYER 1 has total value of ", str(get_value(a)))
        print("PLAYER 2 has total value of ", str(get_value(b)))

    # announce the winner if there is one
    if win == 0:
        print("\033[32mPLAYER 1 WINS\033[0m")
        game_end = True
        break
    elif win == 1:
        print("\033[32mPLAYER 2 WINS\033[0m")
        game_end = True
        break
    elif win == 2:
        print("PLAYERS TIE")
        game_end = True
        break

    # move on to the next player's turn
    turn = (turn + 1) % 2
    if turn == 0:
        round += 1
