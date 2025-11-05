import random

print("🎯 Welcome to the Number Guessing Game!")

while True:
    num = random.randint(1, 100)
    guess = None
    attempts = 0

    print("\nI've chosen a number between 1 and 100. Can you guess it?")

    while guess != num:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < num:
                print("Too low! Try again.")
            elif guess > num:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
        except ValueError:
            print("Please enter a valid number!")

    # Ask if user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again not in ('yes', 'y'):
        print("Thanks for playing! 👋 Goodbye!")
        break
