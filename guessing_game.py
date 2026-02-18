import random

def main():
    print("===================================")
    print("     🎯 NUMBER GUESSING GAME 🎯")
    print("===================================")
    print("I am thinking of a number between 1 and 100.")
    print("You have 5 attempts to guess the correct number.\n")

    secret_number = random.randint(1, 100)
    attempts = 5

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("⚠ Please enter a number between 1 and 100.\n")
                continue

            if guess == secret_number:
                print("\n🎉 Congratulations! You guessed the correct number!")
                print("🏆 You won the game!")
                return
            elif guess < secret_number:
                print("📉 Too low! Try again.")
            else:
                print("📈 Too high! Try again.")

            attempts -= 1
            print(f"Attempts remaining: {attempts}\n")

        except ValueError:
            print("⚠ Invalid input! Please enter a number.\n")

    print("\n❌ Game Over!")
    print(f"The correct number was: {secret_number}")

if __name__ == "__main__":
    main()
