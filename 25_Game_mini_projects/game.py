import random

def play_game():
    print("\n" + "=" * 40)
    print("Welcome to the Number Guessing Game!")
    print("=" * 40)
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random secret number
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        # 1. Get user input safely
        user_input = input("\nEnter your guess (or type 'quit' to exit): ").strip()
        
        # Check if the player wants to give up
        if user_input.lower() == 'quit':
            print(f"\nGame over! The secret number was {secret_number}.")
            break
            
        # 2. Input Validation (Ensure it's actually an integer)
        try:
            guess = int(user_input)
        except ValueError:
            print("❌ Invalid input! Please enter a valid whole number.")
            continue
            
        # Check if the guess is within boundaries
        if guess < 1 or guess > 100:
            print("⚠️ Out of bounds! Please guess a number between 1 and 100.")
            continue
            
        # 3. Game Logic
        attempts += 1
        
        if guess < secret_number:
            print("🔼 Too low! Try a higher number.")
        elif guess > secret_number:
            print("🔽 Too high! Try a lower number.")
        else:
            print(f"\n🎉 Congratulations! You guessed the number in {attempts} attempts!")
            break

def main():
    while True:
        play_game()
        
        # Ask to replay
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye.")
            break

if _name_ == "_main_":
    main()
