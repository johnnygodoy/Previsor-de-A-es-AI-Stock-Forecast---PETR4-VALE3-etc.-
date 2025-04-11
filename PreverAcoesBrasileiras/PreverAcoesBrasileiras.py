import yfinance as yf
import pandas as pd
import os
from Graficos import grafico_acoes

# Criar pasta para armazenar os dados
if not os.path.exists("dados"):
    os.makedirs("dados")

# Solicita ao usuário os dados
acao_usuario = input("Digite o código da ação (ex: PETR4, VALE3, ITUB4): ").upper()
ano_inicio = input("Digite o ano de início (ex: 2020): ")
ano_fim = input("Digite o ano de fim (ex: 2024): ")

# Chama a função para gerar o gráfico da ação escolhida
grafico_acoes.plotar_grafico(acao_usuario, ano_inicio, ano_fim)

# Lista de ações brasileiras para baixar automaticamente
acoes = ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "BBDC4.SA"]

# Criar um DataFrame para armazenar os dados
todos_dados = {}

# Baixar dados históricos de cada ação
for acao in acoes:
    print(f"Baixando dados para {acao}...")
    dados = yf.download(acao, period="5y", interval="1d")

    # Salvar os dados na pasta 'dados'
    dados.to_csv(f"dados/{acao}.csv")
    
    # Armazenar no dicionário
    todos_dados[acao] = dados

# Exibir os primeiros dados da ação escolhida pelo usuário
acao_usuario_sa = f"{acao_usuario}.SA"  # Adiciona ".SA" se necessário

if acao_usuario_sa in todos_dados:
    print(f"🔍 Primeiros dados da ação {acao_usuario}:")
    print(todos_dados[acao_usuario_sa].head())
else:
    print(f"⚠️ Não foram encontrados dados para a ação {acao_usuario}.")
