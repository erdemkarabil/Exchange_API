import requests

api_key = "2ffa04d7f3d4c097ddfa8cf1"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

base_currency = input("Enter the base currency: ")  # USD
target_currency = input("Enter the target currency: ")  # TRY
amount = float(input(f"How much {base_currency} do you want to exchange:  "))  # Amount in USD

# Make the API request
response = requests.get(api_url + base_currency)

# Parse the returned data as JSON
data = response.json()

# Get the exchange rate for the target currency
exchange_rate = data["conversion_rates"][target_currency]

# Calculate the result
result = amount * exchange_rate
print(f"{amount} {base_currency} = {result} {target_currency}")
