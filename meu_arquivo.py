import pandas as pd
from pprint import pprint
# importar base de dados
tabelas_vendas = pd.read_excel('Vendas.xlsx')

#visualizar a base de dados
#exibe todas as colunas
pd.set_option('display.max_columns', None)
pprint(tabelas_vendas)

# faturamenteo por loja


#quantidade de produtos vendidos por loja



#tiket médio por produto em cada loja



# enviar e-mail com o relatório