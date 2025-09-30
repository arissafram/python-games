import random

# Initialize random number
min_num = 0
max_num = 100

print("!!MIN, MAX:", min_num, max_num)
random_number = random.randint(min_num, max_num)
print("!!RANDOM NUMBER:", random_number)

# Set total number of guesses
initial_num_guesses = 7

# Initialize num actual guesses
current_num_guesses = initial_num_guesses

# Set win boolean
is_correct_guess = False

while current_num_guesses > 0:
  guess = input("Enter a number: ")

  if not guess.isdigit():
    print("> Enter a valid number: ")
    continue
  else:
    guess = int(guess)

  if guess < min_num:
    print("> Enter a number equal to or greater than 0: ")
    continue

  if guess > max_num:
    print("> Enter a number less than or equal to 0: ")
    continue

  current_num_guesses -= 1
  
  print(guess, random_number)
  if guess == random_number:
    is_correct_guess = True
    break
  

# Handle win/lose logic
if is_correct_guess:
  actual_num_guesses = initial_num_guesses - current_num_guesses

  print(f"\nYou win! You guessed the number in {actual_num_guesses} "
    f"{'try' if actual_num_guesses == 1 else 'tries'}")

  print(f"The number is {random_number}")
else:
  print(f"You lose. The number is {random_number}")
