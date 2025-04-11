import matplotlib.pyplot as plt
import yfinance as yf

def plotar_grafico(acao, ano_inicio, ano_fim):
    """Baixa dados da ação e plota o gráfico"""
    
    # Criar string para datas
    data_inicio = f"{ano_inicio}-01-01"
    data_fim = f"{ano_fim}-12-31"

    print(f"Baixando dados da ação {acao} de {data_inicio} até {data_fim}...")

    # Baixar dados da ação
    try:
        dados = yf.download(f"{acao}.SA", start=data_inicio, end=data_fim)
        
        if dados.empty:
            print("⚠️ Nenhum dado encontrado! Verifique o código da ação e tente novamente.")
            return

        # Criar o gráfico
        plt.figure(figsize=(12, 6))
        plt.plot(dados['Close'], label=f"Preço de Fechamento: {acao}")  # Adiciona o nome da ação na legenda
        plt.xlabel("Data")
        plt.ylabel("Preço (R$)")
        plt.title(f"Evolução do Preço da Ação {acao} ({ano_inicio} - {ano_fim})")  # Título com nome da ação
        plt.legend()  # Exibe a legenda no gráfico
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"❌ Erro ao buscar dados: {e}")
