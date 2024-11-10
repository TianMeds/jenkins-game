import random
import argparse
from string import capwords

def play_game(player_choice):
    print("Let's Play Rock Paper Scissors")
    Choices = ["Rock", "Paper", "Scissors"]

    print("""Rules: 
    \nYou should only Pick""")
    for c in Choices:
        print(c)

    player_choice = capwords(player_choice)
    computer_choice = random.choice(Choices)

    print("\nYour Pick is: " + player_choice)
    print("Computer's Pick is: " + computer_choice + "\n")

    if player_choice == computer_choice:
        print("The pick is a draw!")
    elif player_choice == "Rock":
        if computer_choice == "Scissors":
            print("You Win!")
        else:
            print("You Lose!")
    elif player_choice == "Paper":
        if computer_choice == "Rock":
            print("You Win!")
        else:
            print("You Lose!")
    elif player_choice == "Scissors":
        if computer_choice == "Rock":
            print("You Lose!")
        else:
            print("You Win!")
    else:
        print("Invalid Option")

def main():
    # Set up argparse to handle command-line arguments
    parser = argparse.ArgumentParser(description="Play Rock Paper Scissors")
    parser.add_argument('--choice', type=str, required=True, help='Your choice: Rock, Paper, or Scissors')

    args = parser.parse_args()
    
    play_game(args.choice)

if __name__ == "__main__":
    main()
