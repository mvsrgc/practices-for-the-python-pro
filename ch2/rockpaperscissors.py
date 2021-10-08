# Shoddy procedural code
import random

OPTIONS = ["rock", "paper", "scissors"]


def print_title():
    print("(1) Rock\n(2) Paper\n(3) Scissors")


def get_human_choice(options):
    choice_number = int(input("Enter the number of your choice: "))
    return options[choice_number - 1]


def get_computer_choice(options):
    return random.choice(options)


def print_choice(human_made_choice, choice):
    print(f"{'You' if human_made_choice else 'Computer'} chose {choice}")


def print_win_lose(human_choice, computer_choice, human_beats, human_loses_to):
    if computer_choice == human_loses_to:
        print(f"Sorry, {computer_choice} beats {human_choice}")
    elif computer_choice == human_beats:
        print(f"Yes, {human_choice} beats {computer_choice}")


def print_result(human_choice, computer_choice):
    if human_choice == computer_choice:
        print("Draw!")

    if human_choice == "rock":
        print_win_lose(human_choice, computer_choice, "scissors", "paper")
    elif human_choice == "paper":
        print_win_lose(human_choice, computer_choice, "rock", "scissors")
    elif human_choice == "scissors":
        print_win_lose(human_choice, computer_choice, "paper", "rock")


print_title()

human_choice = OPTIONS[get_human_choice()]
print_choice(True, human_choice)

computer_choice = get_computer_choice(OPTIONS)
print_choice(False, computer_choice)


print_result(human_choice, computer_choice)
