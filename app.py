#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------


import random

options = ['rock', 'paper', 'scissors']
rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
player_score = 0

while True:
    # Prompt the player to enter their choice
    player_choice = input('Enter your choice (rock/paper/scissors): ').lower()

    # Validate the player's choice
    if player_choice not in options:
        print('Invalid choice. Please enter rock, paper, or scissors.')
        continue

    # Generate the computer's choice
    computer_choice = random.choice(options)

    # Determine the winner
    if player_choice == computer_choice:
        result = 'Tie!'
    elif rules[player_choice] == computer_choice:
        result = 'You win!'
        player_score += 1
    else:
        result = 'You lose!'

    # Print the result and update the score
    print(f'You chose {player_choice}. The computer chose {computer_choice}. {result}')
    print(f'Your score: {player_score}')

    # Ask the player if they want to play again
    play_again = input('Do you want to play again? (y/n): ').lower()

    # Validate the player's input
    if play_again != 'y' and play_again != 'n':
        print('Invalid input. Please enter y or n.')
        continue

    # Exit the loop if the player chooses to stop playing
    if play_again == 'n':
        break