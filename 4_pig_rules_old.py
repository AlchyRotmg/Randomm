#!/usr/bin/env python
 
import random
import time
import os

rules_txt = 'rules.txt'

def rules():
    with open(rules_txt, 'r') as r:
        for line in r.readlines():
            print(line, end = '')

def random_roll(number):
    return random.randint(1, number)

def playgame():
    rules()
    print("\nIt's time to play pig!")
    players = [0,0]
    turn = 0
    while players[0] <= 20 and players[1] <= 20: #or turn + players[0] >= 20 and turn + players[1] >= 20
        response = input("Player 1: Roll or hold? (r/h): ").lower()
        
        if response == 'x':
            break

        elif response == 'r':
            roll = random_roll(6)
            if roll == 1:
                turn = 0
                print(f"\nRoll: {roll}. Lowball! -{turn} points, end turn.\n")
            else:
                turn += roll
                print(f"\nRoll: {roll}\nTurn Score: {turn}\n") 
                continue
        else: 
            players[0] += turn
            print(f"Player 1 score: {players[0]}\n")
        if players[0] >= 20 or turn >= 20:
            break
        response2 = input("Player 2: Roll or hold? (r/h): ")
        if response2 == 'x':
            break
        if response2 == 'r':
            while True:
                roll = random_roll(6)
                if roll == 1:
                    turn = 0
                    print(f"\nRoll: {roll}. Lowball! -{turn} points, end turn.\n")
                    break
                else:
                    turn += roll
                    print(f"Roll: {roll}\nTurn Score: {turn}")
                    response2 = input("Player 2: Roll or hold? (r/h): ").lower()
                    if response2 == 'h':
                        players[1] += turn
                        print(f"Player 2 score: {players[1]}")
                        if players[1] >= 20 or turn >= 20:
                            turn = 0
                            break
                    elif response2 == 'x':
                        break
                break

    if players[0] > players[1]:
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")
    print("Game over.\n")

def main():
    playgame()
    while (replay := input(f"Play again? (y/n): ")).lower() != 'n':
        main()
    print("Goodbye!")

if __name__ == '__main__':
    main()