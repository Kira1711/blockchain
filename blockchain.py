import requests
import time


API_URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

def get_bitcoin_price():
    """Fetches the latest Bitcoin price from Binance API"""
    try:
        response = requests.get(API_URL, timeout=5)  
        response.raise_for_status()  
        data = response.json()
        return float(data["price"])  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    print("Fetching live Bitcoin price from Binance...\n")
    while True:
        price = get_bitcoin_price()
        if price:
            print(f"💰 Bitcoin Price: ${price:,.2f} USD")
        else:
            print("⚠️ Failed to fetch price. Retrying in 10 seconds...")
        
        time.sleep(10) 

if __name__ == "__main__":
    main()


