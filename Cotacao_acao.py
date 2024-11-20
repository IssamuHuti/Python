# cotacao de 1 acao

import yfinance as yf
from pandas_datareader import data as web
import matplotlib.pyplot as plt

# Dados do índice Bovespa
df_bvsp = yf.download('^BVSP', start='2020-02-20', end='2021-02-20')
df_bvsp["Adj Close"].plot(figsize=(10, 5), title="Índice Bovespa (^BVSP)")
print(df_bvsp)
plt.show()

# Dados da PETR4
df_petr4 = yf.download('PETR4.SA', start='2020-02-20', end='2021-02-20')
df_petr4["Adj Close"].plot(figsize=(10, 5), title="PETR4.SA")
print(df_petr4)
plt.show()


# df = web.DataReader(f'PETR4.SA', data_source='yahoo', start=f'02-20-2020', end='02-20-2021')
# display(df)
# df["Adj Close"].plot(figsize=(15, 10))
# plt.show()