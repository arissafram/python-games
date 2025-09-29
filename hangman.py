import random

# Hardcoded words
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']

word = random.choice(words)

# Initial list of guessed lets with underscores, eg. _ _ _ _ _
guessed = ['_'] * len(word)

# Set total number of attempts - this won't change
attempts = 6

# Record guesses as a set to avoid duplicates and look up more efficiently
used_letters = set()

# Initialize game with welcome message & current state
print()
print("Welcome to Hangman!")
print("Word: ", " ".join(guessed))
print("Attempts left:", attempts)
print("Used letters:", " ".join(sorted(used_letters)))

guess = input("Guess a letter: ").lower()

while attempts > 0 and "_" in guessed:
    # Display current state
        print("\nWord: ", " ".join(guessed))
        print("Attempts left:", attempts)
        print("Used letters:", " ".join(sorted(used_letters)))

    # Get and validate guess
        # is guess a letter
        # if not, print error message - not a letter

        # if guess is multiple characters
        # print error message - not a single letter

        # is guess in used_letters
        # if yes, print error message - already guessed

    # Process valid guess
        # if guess is in word, 
        # update guessed
        # if guess is not in word, 
        # decrement attempts
        # and add to used_letters

    # Update game state
        print("\nWord: ", " ".join(guessed))
        print("Attempts left:", attempts)
        print("Used letters:", " ".join(sorted(used_letters)))



# Final win/loss message after loop is over
# End of game
if "_" not in guessed:
    print("\n🎉 You win! The word was:", word)
else:
    print("\n💀 Game over! The word was:", word)
