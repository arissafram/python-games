import random

# Hardcoded words
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Select a random word from the list
word = random.choice(words)

# Initialize list of guessed letters with underscores, eg. _ _ _ _ _
correct_guesses = ['_'] * len(word)

# Initialize number of attempts - this won't change
attempts = 6

# Initialize set of used letters to avoid duplicates and look up more efficiently
used_letters = set()

# Initialize game with welcome message & current state
print("\nWelcome to Hangman!")
print("\nWord: ", " ".join(correct_guesses))
print("Attempts left:", attempts)
print("Used letters:", " ".join(sorted(used_letters)))

# Main game loop 
# Run this until correct_guesses doesn't contain any underscores or attempts run out
while attempts > 0 and "_" in correct_guesses:
  # Prompt user for guess
  guess = input("Guess a letter: ").lower()

  # check if guess is a letter
  if not guess.isalpha():
    print("> Please enter a valid letter")
    continue
  
  # Check if guess is a single letter
  if len(guess) > 1:
    print("> Please enter a single letter")
    continue

  # Check if guess has already been used
  if guess in used_letters:
    print("> You already guessed that letter")
    continue

  # Add guess to used_letters
  used_letters.add(guess)

  # Process valid guess
  if guess in word:
    # Loop over correct_guesses and replace underscore with current letter
    for i,letter in enumerate(word):
      if letter == guess:
        correct_guesses[i] = letter

  else:
    # If guess is not in word, decrement attempts
    attempts -= 1

  # Present new game state to user
  print("\nWord: ", " ".join(correct_guesses))
  print("Attempts left:", attempts)
  print("Used letters:", " ".join(sorted(used_letters)))


# Display final game state
if "_" not in correct_guesses:
  print("\nYou win! The word was:", word.upper())
else:
  print("\nGame over! The word was:", word.upper())
