import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    # atribuindo valor no 'text' da linha 28 assim que o botão da linha 25 for executado    
    texto_resposta['text'] = f''' 
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

janela = Tk() # cria janela, o tamanho varia conforme vai incluindo itens
janela.title("Cotação Atual de Moedas")
# janela.geometry('400x300') # informa o tamanho da janela
texto = Label(janela, text="Clique no botão para ver as cotações de moedas") # Label informa texto dentro da janela, 
                                                                             # na janela criada na variável "janela"
texto.grid(column=0, row=0, padx=10, pady=10) # informa a posição do texto na janela, e o espaçamento do texto com os demais itens

botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes) # criação do botão
botao.grid(column=0, row=1, padx=10, pady=10) # informa a posição do botão na janela

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)


janela.mainloop() # força a janela criada a ficar aberta até rodar essa linha