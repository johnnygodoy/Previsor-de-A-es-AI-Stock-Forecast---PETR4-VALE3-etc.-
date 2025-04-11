import plotly.graph_objects as go

def criar_grafico(dados, titulo):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dados.index, y=dados['Close'], name='Preço', line=dict(color='blue')))
    fig.update_layout(title=titulo, xaxis_title="Data", yaxis_title="Preço")
    fig.show()
