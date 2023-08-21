from alpaca.data.live import CryptoDataStream
#%%
API_KEY = "PKU3DDFUNXYSUF752QK4"
SECRET_KEY = "Pm44X3n38o6BI9Zjy9eFsWrwvsEOzo8vExDbaPyV"

# Initiate class
crypto_stream = CryptoDataStream(API_KEY, SECRET_KEY)
#%%
async def bar_callback(bar):
    for property_name, value in bar:
        print(f"\"{property_name}\": {value}")

# Subscribing to bar event
symbol = "BTC/USD"
crypto_stream.subscribe_bars(bar_callback, symbol)

crypto_stream.run()