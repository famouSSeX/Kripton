with open("pairs_BTC.txt", "r") as file:
    btc_markets = [line.strip() for line in file]
print(btc_markets)