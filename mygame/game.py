import random
import argparse
from string import capwords

print("Let's Play Rock Paper Scissors")

def main(player_choice=None, player_name="Player"):
    choices = ["Rock", "Paper", "Scissors"]

    if player_choice is None:
        print("You should provide a choice in a CI/CD pipeline.")
        return

    computer_choice = random.choice(choices)
    player_choice = capwords(player_choice)

    print(f"\n{player_name}'s pick is: {player_choice}")
    print(f"Computer's pick is: {computer_choice}\n")

    if player_choice == computer_choice:
        print("It's a draw!")
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
        if computer_choice == "Paper":
            print("You Win!")
        else:
            print("You Lose!")
    else:
        print("Invalid Option")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play Rock Paper Scissors in Jenkins.")
    parser.add_argument("--name", type=str, default="Player", help="Name of the player.")
    parser.add_argument("--choice", type=str, choices=["Rock", "Paper", "Scissors"], required=True, help="Your choice.")
    args = parser.parse_args()

    main(player_choice=args.choice, player_name=args.name)
