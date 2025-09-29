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

while attempts > 0 and "_" in guessed:
  # Display current state
  print("\nWord: ", " ".join(guessed))
  print("Attempts left:", attempts)
  print("Used letters:", " ".join(sorted(used_letters)))

  # Get and validate guess
  guess = input("Guess a letter: ").lower()

  # is guess a letter
  if not guess.isalpha():
    print("Please enter a valid letter")
    continue
  
  if len(guess) > 1:
    print("Please enter a single letter")
    continue

  if guess in used_letters:
    print("You already guessed that letter")
    continue


  # for testing,decrement attempts
  attempts -= 1
  used_letters.add(guess)

  # Process valid guess
  # if guess is in word, 
  # update guessed
  # if guess is not in word, 
  # and add to used_letters

  # Present game state to user
  print("\nWord: ", " ".join(guessed))
  print("Attempts left:", attempts)
  print("Used letters:", " ".join(sorted(used_letters)))



# Final win/loss message after loop is over
# End of game
if "_" not in guessed:
  print("\n🎉 You win! The word was:", word)
else:
  print("\n💀 Game over! The word was:", word)
