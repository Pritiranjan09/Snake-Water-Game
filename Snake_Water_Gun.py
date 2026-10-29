```python
import random

# Check the winner of a round
def check_winner(user, computer):
    if user == computer:
        return "Draw"

    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        return "Player"

    else:
        return "Computer"


# Display match history
def show_history(history):
    print("\n========== MATCH HISTORY ==========")

    if not history:
        print("No matches played yet.")
        return

    for i, match in enumerate(history, start=1):
        print(
            f"Round {i}: {match['player_choice']} vs "
            f"{match['computer_choice']} -> {match['result']}"
        )


# Main game
def play_game():
    choices = ["snake", "water", "gun"]
    history = []

    player_name = input("Enter your name: ").strip()

    if not player_name:
        player_name = "Player"

    total_matches = 0
    total_wins = 0
    total_losses = 0
    total_draws = 0

    print(f"\nWelcome, {player_name}! 🐍")
    print("Let's play Snake, Water, Gun!")
    print("First to 3 wins takes the match.")
    print("You can also quit between rounds.")

    while True:
        player_score = 0
        computer_score = 0
        match_round = 0

        while match_round < 5:
            print("\n-------------------------------")
            print(f"Match Round: {match_round + 1}/5")
            print(f"{player_name}: {player_score}")
            print(f"Computer: {computer_score}")

            print("\nChoose your move:")
            print("1. Snake")
            print("2. Water")
            print("3. Gun")
            print("4. Quit Game")

            choice = input("Enter your choice (1-4): ").strip()

            if choice == "4":
                print("\nThanks for playing!")
                print(f"Matches completed: {total_matches}")
                print(f"Your wins: {total_wins}")
                print(f"Your losses: {total_losses}")
                print(f"Draw rounds: {total_draws}")

                if total_wins + total_losses > 0:
                    percentage = (
                        total_wins / (total_wins + total_losses)
                    ) * 100
                    print(f"Your win percentage: {percentage:.2f}%")
                else:
                    print("Your win percentage: 0.00%")

                show_history(history)
                return

            elif choice == "1":
                player_choice = "snake"

            elif choice == "2":
                player_choice = "water"

            elif choice == "3":
                player_choice = "gun"

            else:
                print("Invalid choice! Try again.")
                continue

            computer_choice = random.choice(choices)
            result = check_winner(player_choice, computer_choice)

            print(f"\n{player_name} chose: {player_choice}")
            print(f"Computer chose: {computer_choice}")

            if result == "Player":
                print(f"🎉 {player_name} wins this round!")
                player_score += 1
                total_wins += 1
                round_result = f"{player_name} wins"

            elif result == "Computer":
                print("💻 Computer wins this round!")
                computer_score += 1
                total_losses += 1
                round_result = "Computer wins"

            else:
                print("🤝 It's a draw!")
                total_draws += 1
                round_result = "Draw"

            match_round += 1

            history.append({
                "player_choice": player_choice,
                "computer_choice": computer_choice,
                "result": round_result
            })

            if player_score == 3 or computer_score == 3:
                break

        total_matches += 1

        print("\n========== MATCH RESULT ==========")
        print(f"{player_name}: {player_score}")
        print(f"Computer: {computer_score}")

        if player_score > computer_score:
            print(f"🏆 Congratulations, {player_name}! You won the match!")

        elif computer_score > player_score:
            print("💻 Computer won the match. Better luck next time!")

        else:
            print("🤝 The match ended in a draw!")

        print("\n========== STATISTICS ==========")
        print(f"Matches completed: {total_matches}")
        print(f"Rounds won by you: {total_wins}")
        print(f"
```
