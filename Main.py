import ccxt
import time

# инициализация бирж
exchange_binance = ccxt.binance({
    'apiKey': '',
    'secret': '',
})

exchange_huobi = ccxt.huobipro({
    'apiKey': '',
    'secret': '',
})

# задержка в 1 секунду для избежания блокировки биржей
time.sleep(1)

# получение цены покупки BTC на Binance
btc_buy_price_binance = exchange_binance.fetch_ticker('BTC/USDT')['bid']

# получение цены продажи BTC на Huobi
btc_sell_price_huobi = exchange_huobi.fetch_ticker('BTC/USDT')['ask']

# вычисление спреда для пары BTC/USDT
btc_spread = ((float(btc_sell_price_huobi) - float(btc_buy_price_binance)) / float(btc_buy_price_binance)) * 100

# получение цены покупки USDT на Binance
p2p_markets_binance = exchange_binance.load_markets()
usdt_buy_price_binance = p2p_markets_binance['usdt']['info']['price']

# получение цены продажи USDT на Huobi
usdt_sell_price_huobi = exchange_huobi.fetch_ticker('USDT/BTC')['ask']

# вычисление спреда для пары USDT/BTC
usdt_spread = ((float(usdt_sell_price_huobi) - float(usdt_buy_price_binance)) / float(usdt_buy_price_binance)) * 100

# получение цены покупки ETH на Binance
eth_buy_price_binance = exchange_binance.fetch_ticker('ETH/USDT')['bid']

# получение цены продажи ETH на Huobi
eth_sell_price_huobi = exchange_huobi.fetch_ticker('ETH/USDT')['ask']

# вычисление спреда для пары ETH/USDT
eth_spread = ((float(eth_sell_price_huobi) - float(eth_buy_price_binance)) / float(eth_buy_price_binance)) * 100

# получение цены покупки USDT на Binance
usdt_buy_price_binance = exchange_binance.fetch_ticker('USDT/ETH')['bid']

# получение цены продажи USDT на Huobi
usdt_sell_price_huobi = exchange_huobi.fetch_ticker('USDT/ETH')['ask']

# вычисление спреда для пары USDT/ETH
usdt_spread = ((float(usdt_sell_price_huobi) - float(usdt_buy_price_binance)) / float(usdt_buy_price_binance)) * 100

# вывод результатов
print('-----------------------')
print(f'[BUY] BTC->binance ({btc_buy_price_binance})')
print(f'[SELL] BTC->huobi ({btc_sell_price_huobi}) | SPREAD: {btc_spread:.2f}%')
print('-----------------------')
print(f'[BUY] USDT->binance ({usdt_buy_price_binance})')
print(f'[SELL] USDT->huobi ({usdt_sell_price_huobi}) | SPREAD: {usdt_spread:.2f}%')
print('-----------------------')
print(f'[BUY] ETH->binance ({eth_buy_price_binance})')
print(f'[SELL] ETH->huobi ({eth_sell_price_huobi}) | SPREAD: {eth_spread:.2f}%')
print('-----------------------')
print(f'[BUY] USDT->binance ({usdt_buy_price_binance})')
print(f'[SELL] USDT->huobi ({usdt_sell_price_huobi}) | SPREAD: {usdt_spread:.2f}%')
print('-----------------------')