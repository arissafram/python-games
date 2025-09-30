import random

MAX_GUESSES = 7
MAX_NUMBER = 100
MIN_NUMBER = 1

# Prompt user and validate innput
def get_valid_guess(min_num, max_num):
  while True:
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

    return guess

# Update the range based on the guess
def update_range(guess, random_number, min_num, max_num):
  if guess > random_number:
    max_num = guess - 1
    print(f"\n> Too high. Guess again between {min_num} and {max_num}:")
  else:
    min_num = guess + 1
    print(f"\n> Too low. Guess again between {min_num} and {max_num}:")

  return min_num, max_num

# Main game loop
def play_game():
  initial_num_guesses = MAX_GUESSES
  current_num_guesses = initial_num_guesses
  is_correct_guess = False
  max_num = MAX_NUMBER
  min_num = MIN_NUMBER
  random_number = random.randint(min_num, max_num)

  #Main game loop
  while current_num_guesses > 0:
    guess = get_valid_guess(min_num, max_num)
    current_num_guesses -= 1

    if (guess == random_number):
      is_correct_guess = True
      break
    else:
      min_num, max_num = update_range(guess, random_number, min_num, max_num)  

  # Handle win/lose logic
  if is_correct_guess:
    actual_num_guesses = initial_num_guesses - current_num_guesses
    print(f"\nYou win! You guessed the number in {actual_num_guesses} "
          f"{'try' if actual_num_guesses == 1 else 'tries'}")
    print(f"The number is {random_number}")
  else:
    print(f"You lose. The number is {random_number}")

# Main function
def main():
  print()
  print("Welcome to Guess The Number!")
  print("I'm thinking of a number between 1 and 100")
  print("You have 7 tries to guess it, I'll tell you if you're higher/lower")
  play_game()


if __name__ == "__main__":
  main()
