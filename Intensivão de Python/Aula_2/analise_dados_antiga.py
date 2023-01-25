"""
Análise de Dados com Python
Desafio:
Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.

O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.

Isso representa uma perda de milhões para a empresa.

O que a empresa precisa fazer para resolver isso?

Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing
Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

"""

import pandas as pd
import plotly.express as px

df = pd.read_csv('telecom_users.csv')

#limpar dados
#axis=0 linha; axis=1 coluna
df = df.drop('Unnamed: 0', axis=1)

#resolver valores sendo reconhecidos de for errada (valores que eram pra ser int mas estao como object)
df['TotalGasto'] = pd.to_numeric(df['TotalGasto'], errors='coerce')#coerce, forçar a barra, se for impossivel virar numero, vira NaN






#Análise Inicial
#print(df['Churn'].value_counts())
#print(df['Churn'].value_counts(normalize=True).map('{:.2%}'.format))


#Análise Detalhada
#criar grafico
coluna = 'TipoContrato'
grafico = px.histogram(df, x=coluna, color='Churn', text_auto=True)
#mostrar grafico
grafico.show()


#Para cada coluna da minha tabela eu quero um grafico
"""for coluna in df.columns:
    grafico = px.histogram(df, x=coluna, color='Churn', text_auto=True)
    grafico.show()"""


"""
- Clientes que tem familias maiores tendem a cancelar menos
    - Promoções diferenciadas para mais pessoas da mesma familia

- Os clientes nos primeiros meses tem uma tendencia MUITO maior a cancelar
    - Pode ser algum marketing mt agressivo
    - Pode ser que a experiencia nos primeiros meses eteja ruim
    - Posso fazer uma promoção que no primeiro ano é mais barato
    
- Tem algum problema no serviço de fibra
- Quanto mais serviços os clientes tem, menos ele cancela
    - Podemos oferecer mais serviços de graça ou por um preço menor

- Quase todos os cancelamentos estão no anual
    - Oferecer descontos no anual e no de 2 anos
    
- No boleto o cancelamento é muito maior
    - Oferecer um desconto no debito automatico
"""