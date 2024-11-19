# cotacao de 1 acao

import yfinance as yf
from pandas_datareader import data as web
import matplotlib.pyplot as plt

# df = web.DataReader(f'^BVSP', data_source='yahoo', start=f'02-20-2020', end='02-20-2021')
# display(df)
# df["Adj Close"].plot(figsize=(15, 10))
# plt.show()

# df = web.DataReader(f'PETR4.SA', data_source='yahoo', start=f'02-20-2020', end='02-20-2021')
# display(df)
# df["Adj Close"].plot(figsize=(15, 10))
# plt.show()

# Para corrigir possíveis erros em versões antigas
yf.pdr_override()

# Dados do índice Bovespa
# df_bvsp = yf.download('^BVSP', start='2020-02-20', end='2021-02-20')
# df_bvsp["Adj Close"].plot(figsize=(15, 10), title="Índice Bovespa (^BVSP)")
df_bvsp = web.DataReader('^BVSP', data_source='yahoo', start='2020-02-20', end='2021-02-20')
df_bvsp["Adj Close"].plot(figsize=(15, 10), title="Índice Bovespa (^BVSP)")
plt.show()

# Dados da PETR4
# df_petr4 = yf.download('PETR4.SA', start='2020-02-20', end='2021-02-20')
# df_petr4["Adj Close"].plot(figsize=(15, 10), title="PETR4.SA")
df_petr4 = web.DataReader('PETR4.SA', data_source='yahoo', start='2020-02-20', end='2021-02-20')
df_petr4["Adj Close"].plot(figsize=(15, 10), title="PETR4.SA")
plt.show()


# pegando cotação de uma carteira de ação em um intervalo de datas especificos 

# data_inicial = "01/01/2020"
# data_final = "01/01/2021"

# empresas_df = pd.read_excel("Empresas.xlsx")
# display(empresas_df)

# for empresa in empresas_df['Empresas']: 
#     print(f"{empresa}:")
#     df = web.DataReader(f'{empresa}.SA', data_source='yahoo', start=data_inicial, end=data_final)
#     display(df)
#     df["Adj Close"].plot(figsize=(15, 10))
#     plt.show()

