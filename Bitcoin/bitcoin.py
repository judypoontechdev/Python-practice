## Task Overview
#The goal of this task was to create a command-line script (`bitcoin.py`) that 
# accepts the number of Bitcoins as an argument, fetches the real-time Bitcoin 
# price in USD using the CoinCap v3 API via the `requests` library, calculates 
# the total cost, and formats the output as currency.
import os
import requests
import sys
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Check whether the user has input the amount of bitcoin
if len(sys.argv) != 2:
    sys.exit('Missing command-line argument')

# Check whether the user's input can be converted to float
try:
    bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')

# Fetch the current bitcoin price using API
try:
    # Get api key
    api_key = os.getenv('COINCAP_API_KEY')

    response = requests.get(f'https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}')
except requests.RequestException:
    sys.exit()
else:
    output = response.json()

# Extract the usd price
usd = float(output['data']['priceUsd'])

# Total price
total_price = usd * bitcoin
print(f'${total_price:,.4f}')