#Desafio inicial de analíse de dados para identificar e ajudar 
# a loja de bermudas a vender mais

import pandas as pd
from IPython.display import display

tabela = pd.read_excel("Vendas.xlsx")
#display(tabela)

faturamento_total= tabela["Valor Final"].sum()
#print(faturamento_total)

faturamento_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum() #uso o colchete duas vezes para buscar as duas colunas
#display(faturamento_loja)

#groupby é para agrupar as colunas que são iguais e o sum é para somar o resto que sobrou que são as colunas de valores

faturamento_produto = tabela[["ID Loja", "Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
display(faturamento_produto)
#E aqui pelos dados comprovados vemos que a Bermuda Liso é uma solução para aumentar vendas nas lojas