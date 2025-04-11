#Indicadores t�cnicos (SMA, RSI, MACD) que ajudam a entender a tend�ncia do mercado.
#Calcular M�dias M�veis, RSI e MACD.
import pandas as pd

def calcular_indicadores(dados):
    # M�dia M�vel Simples (SMA)
    dados['SMA50'] = dados['Close'].rolling(window=50).mean()
    dados['SMA200'] = dados['Close'].rolling(window=200).mean()

    # RSI (�ndice de For�a Relativa)
    def calcular_rsi(data, period=14):
        delta = data.diff()
        ganho = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        perda = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = ganho / perda
        return 100 - (100 / (1 + rs))

    dados['RSI'] = calcular_rsi(dados['Close'])

    # MACD (Moving Average Convergence Divergence)
    exp12 = dados['Close'].ewm(span=12, adjust=False).mean()
    exp26 = dados['Close'].ewm(span=26, adjust=False).mean()
    dados['MACD'] = exp12 - exp26
    dados['Signal'] = dados['MACD'].ewm(span=9, adjust=False).mean()

    return dados




