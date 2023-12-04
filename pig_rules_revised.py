#!/usr/bin/env python

#this one was a real thinker, seperating turn into a seperate function that changes based on playgame() variables was the answer.
#needed to change the player score and player value with a current player variable
# ***RESEARCH/REFINE FUNCTION PASSING***

import random

rules_txt = 'rules.txt'

def rules():
    with open(rules_txt, 'r') as r:
        for line in r.readlines():
            print(line, end='')

def random_roll(number):
    return random.randint(1, number)

def player_turn(current_player, players, turn): #passes 3 variables from playgame() and returns them to modify player turn/score
    while True:
        response = input(f"Player {current_player}: Roll or hold? (r/h): ").lower()

        if response == 'x':
            return 'x' #returns x to 'if' statement in playgame()

        elif response == 'r':
            roll = random_roll(6)
            if roll == 1:
                print(f"\nRoll: {roll}. Lowball! -{turn} points, end turn.\n")
                return 0 
            else:
                turn += roll
                print(f"\nRoll: {roll}\nTurn Score: {turn}\n")
        else: 
            players[current_player - 1] += turn #calculates players turn score and prints the player and value
            print(f"Player {current_player} score: {players[current_player - 1]}\n")
            return 0

def playgame():
    rules()
    print("\nIt's time to play pig!")
    players = [0, 0]
    current_player = 1

    while players[0] <= 20 and players[1] <= 20: #constantly checks if either player has won by accessing players[] score, win = 20
        turn = 0 
        turn = player_turn(current_player, players, turn) #uses turn variable to return a string

        if turn == 'x':
            break

        if players[current_player - 1] >= 20: #ends game if player is larger or equal to 20
            break

        current_player = 3 - current_player #this line switches current_player by subtracting current_player from 3 (3-1 = 2 | 3-2 = 1)

    if players[0] > players[1]:
        print("Player 1 Wins!")
    
    else:
        print("Player 2 Wins!")
    print("Game over.\n")

def main():
    playgame()
    while (replay := input(f"Play again? (y/n): ")).lower() != 'n': #simple assignment loop to repeat the game, no predefined variable needed
        main()
    print("Goodbye!")

if __name__ == '__main__':
    main()