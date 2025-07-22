# NOTE of uselessneess: this is a pointless because the api I found only gets gives price data in the last year so older requests will fail:(

import requests
from datetime import datetime

def main():
    # Get user input
    while True:
        have_usd = input("How much money in USD do you wish you had invested in bitcoin? ")
        try:
            have_usd = float(have_usd)
            break  # Exit the loop if value is a float
        except ValueError:
            print("Please enter a valid amount of money.")

    while True:
        time_inv = input("When do you wish you had purchased bitcoin? (YYYY/MM/DD) ")
        try:
            # Validate date format
            date_obj = datetime.strptime(time_inv, "%Y/%m/%d")
            break
        except ValueError:
            print("Please enter a valid date in YYYY/MM/DD format.")

    # Calculate the final amount of bitcoin
    final_usd = bitcalc(have_usd, date_obj)

    # Print the result or an error message
    if final_usd is None:
        print("Sorry, could not retrieve Bitcoin price for that date. Please try a different date.")
    else:
        print(f"You would have had ${final_usd:.2f} in bitcoin.")

def bitcalc(have_usd, date_obj):
    # Use CoinGecko API to get historical BTC price for the given date
    date_str = date_obj.strftime("%d-%m-%Y")  # CoinGecko expects DD-MM-YYYY
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/history?date={date_str}"
    try:
        response = requests.get(url)
        data = response.json()
        if 'market_data' not in data or 'current_price' not in data['market_data'] or 'usd' not in data['market_data']['current_price']:
            print("DEBUG: CoinGecko API response:", data)  # Debug output
            return None
        price = data['market_data']['current_price']['usd']
    except Exception as e:
        print("Error fetching data from CoinGecko:", e)
        return None
    # Calculate how much BTC the user could have bought
    btc_amount = have_usd / price
    # Get current BTC price
    try:
        current_data = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()
        current_price = current_data['bitcoin']['usd']
    except Exception as e:
        print("Error fetching current BTC price:", e)
        return None
    # Calculate current value of that BTC
    return btc_amount * current_price

if __name__ == "__main__":
    main()

