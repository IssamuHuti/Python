# pegando cotação de uma carteira de ação em um intervalo de datas especificos 

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

data_inicial = "2020-02-20"
data_final = "2021-02-20"

empresas_df = ['ITUB3', 'PETR4', 'VALE3', 'MGLU3']

dados_consolidados = pd.DataFrame()

for empresa in empresas_df: 
    print(f"{empresa}:")
    df = yf.download(f'{empresa}.SA', start=data_inicial, end=data_final)
    if not df.empty:
        dados_consolidados[empresa] = df['Adj Close']
        print(df[['Adj Close']].tail())
    else:
        print(f"Nenhum dado encontrado para {empresa}.")

if not dados_consolidados.empty:
    dados_consolidados.plot(figsize=(10, 5), title="Cotações Consolidadas")
    plt.xlabel("Data")
    plt.ylabel("Preço Ajustado (R$)")
    plt.legend(title="Empresas")
    plt.show()
else:
    print("Nenhum dado foi consolidado.")

