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

