import random

def roll_die():
    return random.randint(1, 6)

def play_pig():
    print("Welcome to The Game of Pig!")

    overall_score = 0
    round_score = 0

    while overall_score < 100:
        print(f"\nYour overall score: {overall_score}")
        print(f"Your current round score: {round_score}")

        choice = input("Do you want to roll or bank? (r/b): ").lower()

        if choice == 'r':
            roll = roll_die()
            print(f"You rolled a {roll}!")

            if roll == 1:
                print("You rolled a 1. Round score resets to 0.")
                round_score = 0
                continue
            else:
                round_score += roll
                print(f"Your round score is now {round_score}.")

        elif choice == 'b':
            overall_score += round_score
            round_score = 0
            print("You banked your points!")
            print(f"Your overall score is now {overall_score}.")

        else:
            print("Invalid choice. Please enter 'r' to roll or 'b' to bank.")

    print("\nCongratulations! You've reached 100 points and won the game!")


if __name__ == "__main__":
    play_pig()