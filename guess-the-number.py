import random

# Initialize random number
random_number = random.randint(0, 100)
print("FOR TESTING:", random_number)

# Set total number of guesses
total_num_guesses = 7

# Initialize num actual guesses
num_guesses = total_num_guesses

# Set win boolean
isCorrectGuess = False

while num_guesses > 0:
  guess = input("Enter a number: ")

  if not guess.isdigit():
    print("> Enter a valid number: ")
    continue
  else:
    guess = int(guess)

  if guess < 0:
    print("> Enter a number equal to or greater than 0: ")
    continue

  if guess > 100:
    print("> Enter a number less than or equal to 0: ")
    continue

  num_guesses -= 1
  
  print(guess, random_number)
  if guess == random_number:
    isCorrectGuess = True
    break

# Handle win/lose logic
if isCorrectGuess:
  print("\n You win! You guessed the number in {total_num_guesses} - {num_guesses} tries")
  print("The number is {random_number}")
else:
  print("You lose. The number is {random_number}")
