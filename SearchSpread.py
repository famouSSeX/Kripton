import ccxt

#pairsBTC = open("pairs_BTC.txt", "r")
with open("pairs_BTC.txt", "r") as file:
    btc_markets = [line.strip() for line in file]
print(btc_markets)
# создание объекта для работы с биржей Binance
exchange = ccxt.binance({
    'enableRateLimit': True,
    'rateLimit': 1500,
})

# получение списка всех доступных рынков на бирже Binance
#markets = exchange.load_markets()

# нахождение всех пар, связанных с BTC

#btc_markets = [market for market in markets if 'BTC' in market]
#btc_markets = [for line in pairsBTC]


# получение цены покупки BTC в USDT
btc_buy_price_usdt = exchange.fetch_ticker('BTC/USDT')['bid']

# получение цены продажи BTC в USDT
btc_sell_price_usdt = exchange.fetch_ticker('BTC/USDT')['ask']

# вывод результатов
print('-----------------------')
print(f'[BUY] BTC->binance ({btc_buy_price_usdt} USDT)')

# нахождение спредов для всех пар, связанных с BTC
for market in btc_markets:
    coin_buy_price = exchange.fetch_ticker(market)['bid']
    coin_sell_price = exchange.fetch_ticker(market)['ask']
    coin_buy_price_btc = exchange.fetch_ticker(market)['bid']
    coin_sell_price_btc = exchange.fetch_ticker(market)['ask']
    # вычисление спреда для пары на Binance
    coin_spread = ((float(coin_sell_price) * 0.999) - (float(coin_buy_price) * 1.001)) / float(coin_buy_price) * 100

    # вычисление спреда для пары через BTC на Binance
    btc_spread = ((float(coin_sell_price_btc) * 0.999 * float(btc_sell_price_usdt)) - (
                float(coin_buy_price_btc) * 1.001 * float(btc_buy_price_usdt))) / (
                             float(coin_buy_price_btc) * float(btc_buy_price_usdt)) * 100

    # вывод результатов
    print('-----------------------')
    print(f'[BUY] {market}->binance ({coin_buy_price} BTC)')
    print(f'[SELL] {market}->binance ({coin_sell_price} BTC) | SPREAD: {coin_spread:.2f}%')
    print(
        f'[SELL] {market}->BTC ({coin_sell_price_btc} BTC) -> USDT ({coin_sell_price_btc * btc_sell_price_usdt} USDT)')
    print(
        f'[BUY] {market}->BTC ({coin_buy_price_btc} BTC) -> USDT ({coin_buy_price_btc * btc_buy_price_usdt} USDT) | SPREAD: {btc_spread:.2f}%')
    print('-----------------------')