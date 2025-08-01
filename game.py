import time
import random

def __init__():
    pass

# Get rock, paper, or scissors from the CPU
def get_cpu_choice():
    choices = ["Rock", "Paper", "Scissors"]
    choice = random.choice(choices)
    return choice

def game(player_choice):
    time_to_sleep = 0.1
    cpu_choice = get_cpu_choice()
    # player_choice = input("Rock, paper, or scissors? ").capitalize()
    

    if cpu_choice == player_choice:
        print("You tied!")
        time.sleep(time_to_sleep)
    elif (player_choice == "0 Rock" and cpu_choice == "Scissors") or (player_choice == "1 Paper" and cpu_choice == "Rock") or (player_choice == "2 Scissors" and cpu_choice == "Paper"):
        print("You win!")
        time.sleep(time_to_sleep)
    elif player_choice == "3 Nothing":
        pass
    else:
        print("You lose!")
        time.sleep(time_to_sleep)
