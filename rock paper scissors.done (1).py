# This file was created by Daniel Barandica on 09/09/2023

import random

def main():
    print("Play Rock Paper Scissors!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = choose_winner(user_choice, computer_choice)
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(result)

        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break
# intro to game, greets player, organizes presentation of choices for both player and computer, allows for multiple attempts by asking player if they would like to play again

def get_user_choice(): 
    """Get user choice (Rock, Paper, Scissors)"""
    while True:
        user_choice = input("Choose (Rock, Paper, Scissors) ").strip().lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print ("INVALID CHOICE!!!")
# gets your choice, what you can and cannot say    
       
def get_computer_choice():
    """Generate computer's random choice"""
    return random.choice (["rock", "paper", "scissors"])
# gets computer's choice, randomly generated

def choose_winner(user_choice, computer_choice):
    """Determine winner"""
    if user_choice == computer_choice:
        return "Tie!"
    elif((user_choice =="rock" and computer_choice =="scissors") or
         (user_choice == "scissors" and computer_choice == "paper") or
         (user_choice == "paper" and computer_choice == "rock")):
        return "You Win!"
    else:
        return "Computer Wins!"
#determines who wins, based on choice, only winners, no losing comments, positive

if __name__ == "__main__":
    main()