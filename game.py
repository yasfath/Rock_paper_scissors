import random

def get_user_choice():

    choices = ["rock","paper", "scissors"]
    while True:
        user_choice = input("Enter rock, paper, scissors:").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice! please try again.\n ")
    
def get_computer_choice():
    return random.choice(["rock","paper","scissors"])

def decide_winner(user, computer):
    print("DEBUG comparing:", user, "vs", computer)

    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"
    
def play_game():
    user_score = 0
    computer_score = 0
    rounds = 0

    print("Welcome to rock paper scissors Game")
    print("-----------------------------------------")

    while True:
        rounds +=1
        print(f"\n Round {rounds}")

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"computer chose: {computer_choice}")

        result = decide_winner(user_choice,computer_choice)

        if result == "tie":
            print("It is tie")
        elif result == "user":
            print("Ypu win this round!")
            user_score +=1
        else:
            print("Computer wins the round!")
            computer_score +=1

        print("\n Scoreboard")
        print(f"You:{user_score}")
        print(f"computer: {computer_score}")

        play_again = input("\n Do you want to play again? (yes/no):") .lower()
        if play_again !="yes":
            print("\n Game over")
            print("Final results:")
            print(f"Total Rounds:{rounds}")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")

            if user_score > computer_score:
                print ("Overall Winner: You!")
            elif computer_score > user_score:
                print("Overall Winner: Computer!")
            else:
                print("Overall Result: Tie! ")

            print("\n Thanks For Playing")
            break 

play_game()