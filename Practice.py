import random


def roll_die():
    """Simulates rolling a 6-sided die."""
    return random.randint(1, 6)


def player_turn(overall_score, turn_count):
    """Handles the player's turn."""
    round_score = 0
    while True:
        turn_count += 1
        print(f"\nYour overall score: {overall_score}")
        print(f"Your current round score: {round_score}")
        print(f"Player's turn count: {turn_count}")

        choice = input("Do you want to roll or bank? (r/b): ").lower()

        if choice == 'r':
            roll = roll_die()
            print(f"You rolled a {roll}!")

            if roll == 1:
                print("Oh no! You rolled a 1. Round score resets to 0.")
                round_score = 0
                break
            else:
                round_score += roll
                print(f"Your round score is now {round_score}.")

        elif choice == 'b':
            overall_score += round_score
            round_score = 0
            print("You banked your points!")
            print(f"Your overall score is now {overall_score}.")
            break

        else:
            print("Invalid choice. Please enter 'r' to roll or 'b' to bank.")

    return overall_score, turn_count


def computer_turn(overall_score, turn_count):
    """Handles the computer's turn."""
    round_score = 0
    print("\nComputer's turn...")

    while round_score <= 15:
        turn_count += 1
        roll = roll_die()
        print(f"Computer rolled a {roll}!")
        print(f"Computer's turn count: {turn_count}")

        if roll == 1:
            print("Computer rolled a 1. Round score resets to 0.")
            round_score = 0
            break
        else:
            round_score += roll
            print(f"Computer's round score is now {round_score}.")

    if round_score > 0:
        overall_score += round_score
        print("Computer banked its points!")
        print(f"Computer's overall score is now {overall_score}.")

    return overall_score, turn_count


def play_pig():
    """Main function to play the Game of Pig."""
    print("Welcome to the Game of Pig!")

    player_score = 0
    computer_score = 0
    player_turn_count = 0
    computer_turn_count = 0

    while player_score < 100 and computer_score < 100:
        print("\n========================")
        print("Player's turn!")
        player_score, player_turn_count = player_turn(player_score, player_turn_count)

        if player_score >= 100:
            break

        print("\n========================")
        print("Computer's turn!")
        computer_score, computer_turn_count = computer_turn(computer_score, computer_turn_count)

    print("\n========================")
    print("Game Over!")
    print(f"Final Scores - You: {player_score}, Computer: {computer_score}")
    print(f"Final Turn Counts - Player: {player_turn_count}, Computer: {computer_turn_count}")

    if player_score >= 100 and computer_score >= 100:
        if player_score > computer_score:
            print("Congratulations! You win with a higher score!")
        elif computer_score > player_score:
            print("Computer wins with a higher score. Better luck next time!")
        else:
            print("It's a tie! Both scored equally over 100.")
    elif player_score >= 100:
        print("Congratulations! You reached 100 points first and won the game!")
    else:
        print("Computer reached 100 points first. Better luck next time!")


if __name__ == "__main__":
    play_pig()
