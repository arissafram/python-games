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


getData("https://restcountries.com/v3.1/all?fields=name,capital")
