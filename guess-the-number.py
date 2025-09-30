import random

# Initialize random number
min_num = 1
max_num = 100

# Set random number
random_number = random.randint(min_num, max_num)

# Set total number of guesses
initial_num_guesses = 7

# Initialize num actual guesses
current_num_guesses = initial_num_guesses

# Set win boolean
is_correct_guess = False

while current_num_guesses > 0:
  guess = input("Enter a number: ")

  # Ensure input is a valid number
  try:
    guess = int(guess)
  except ValueError:
    print("> Enter a valid number")
    continue

  if guess < min_num:
    print(f"> Enter a number equal to or greater than {min_num}: ")
    continue

  if guess > max_num:
    print(f"> Enter a number less than or equal to {max_num}: ")
    continue

  current_num_guesses -= 1
  
  if guess == random_number:
    is_correct_guess = True
    break
  elif guess > random_number:
    max_num = guess - 1
    print(f"\n> Too high. Guess again between {min_num} and {max_num}:")
  else:
    min_num = guess + 1
    print(f"\n> Too low. Guess again between {min_num} and {max_num}:")

  

# Handle win/lose logic
if is_correct_guess:
  actual_num_guesses = initial_num_guesses - current_num_guesses

  print(f"\nYou win! You guessed the number in {actual_num_guesses} "
        f"{'try' if actual_num_guesses == 1 else 'tries'}")

  print(f"The number is {random_number}")
else:
  print(f"You lose. The number is {random_number}")
