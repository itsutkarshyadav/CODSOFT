import random

choices = ["r", "p", "s"]

def get_choice_name(choice):
    """Convert choice shorthand to full name."""
    return {"r": "ROCK", "p": "PAPER", "s": "SCISSORS"}.get(choice, "INVALID")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("-----START GAME-----")
        print("\n-> r for ROCK \n-> p for PAPER \n-> s for SCISSORS")
        
        user_choice = input("Enter your choice: ").strip().lower()
        if user_choice not in choices:
            print("Invalid choice. Please choose 'r', 'p', or 's'.\n")
            continue

        # Computer makes its choice after user input
        computer_choice = random.choice(choices)

        print(f"Computer choice is {get_choice_name(computer_choice)} and your choice is {get_choice_name(user_choice)}")

        if computer_choice == user_choice:
            print("It's a tie! Try again...\n")
        
        elif (user_choice == "r" and computer_choice == "s") or \
             (user_choice == "p" and computer_choice == "r") or \
             (user_choice == "s" and computer_choice == "p"):
            print("You Win!")
            user_score += 1
        else:
            print("You Lose!")
            computer_score += 1

        print(f"USER SCORE: {user_score} | COMPUTER SCORE: {computer_score}\n")

        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again == "n":
            break

    print("-----GAME OVER-----")
    print(f"FINAL SCORE -> USER: {user_score} | COMPUTER: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()