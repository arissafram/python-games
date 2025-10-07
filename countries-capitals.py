# supress warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)

# install requests
import requests

def getData(url):
  url = "https://restcountries.com/v3.1/all?fields=name,capital"
  try: 
    response = requests.get(url)
    data = response.json()
    return data
    # handle errors
  
  except:
    print('Something went wrong')
    return None

def play_game():
  data = getData("https://restcountries.com/v3.1/all?fields=name,capital")
  total_countries = len(data)
  num_guesses = 0
  num_correct_guesses = 0

  print('Welcome! When I prompt you with a country, type in the capital')
  while(num_guesses < total_countries):
    current_country = data[num_guesses]['name']['common']
    current_capitals = data[num_guesses]['capital']
    current_capitals = [capital.lower() for capital in current_capitals]
  
    print(f"\nCurrent score: {num_correct_guesses}/{num_guesses}")
    print(current_country)
    guess = input()

    if guess.lower() in current_capitals:
      num_correct_guesses += 1
      
    num_guesses += 1

play_game()

