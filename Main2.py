import ccxt

f = open("pricesBTC.txt","w")

exchange = ccxt.binance()

markets = exchange.load_markets()

for market in markets:
    if "BTC" in market:
        buy_price_binance = exchange.fetch_ticker(str(market))['bid']
        if (buy_price_binance != 0.0):
            sell_price_binance = exchange.fetch_ticker(str(market))['ask']
            f.write("--------------------------" + "\n")
            f.write("Pair: " + str(market) + "\n")
            f.write("Buy: " + str(buy_price_binance) + "\n")
            f.write("Sell: " + str(sell_price_binance) + "\n")
        else:
            continue

