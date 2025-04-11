#prever preços futuros baseado em dados históricos.

import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def treinar_modelo(dados):
    scaler = MinMaxScaler(feature_range=(0, 1))
    dados_scaled = scaler.fit_transform(dados[['Close']])

    # Criar dados de treinamento e teste
    X, y = [], []
    for i in range(60, len(dados_scaled)):
        X.append(dados_scaled[i-60:i, 0])
        y.append(dados_scaled[i, 0])

    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    # Dividir em treino e teste (80% treino, 20% teste)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Criar modelo LSTM
    modelo = tf.keras.Sequential([
        tf.keras.layers.LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)),
        tf.keras.layers.LSTM(50, return_sequences=False),
        tf.keras.layers.Dense(25),
        tf.keras.layers.Dense(1)
    ])

    modelo.compile(optimizer='adam', loss='mean_squared_error')

    # Treinar o modelo
    modelo.fit(X_train, y_train, batch_size=16, epochs=20)

    # Avaliar o modelo
    loss = modelo.evaluate(X_test, y_test)
    print(f'🔍 Erro médio quadrático no teste: {loss:.5f}')

    return modelo, scaler
