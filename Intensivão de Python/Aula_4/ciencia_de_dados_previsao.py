"""
Criar um modelo de previsão de vendas com ciencia de dados

Passo a Passo de um Projeto de Ciência de Dados
Passo 1: Entendimento do Desafio
Passo 2: Entendimento da Área/Empresa
Passo 3: Extração/Obtenção de Dados
Passo 4: Ajuste de Dados (Tratamento/Limpeza)
Passo 5: Análise Exploratória
Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)
Passo 7: Interpretação de Resultados

tv, radio, jornal em milhares
vendas em milhoes
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

tabela = pd.read_csv('advertising.csv')

#analise exploratoria (como as coisas estao funcionando)
#calcular correlação (correlação vai de 0 a 1)

#print(tabela.corr())#correlação

# #criar grafico
# sns.heatmap(tabela.corr(), cmap='Greens', annot=True)
#
# #exibe o grafico
# plt.show()



#Criar modelo de previsão
#dividir x e y
y = tabela['Vendas']#quem vc quer prever
x = tabela[['TV', 'Radio', 'Jornal']]#quem sera analisado


#dividr base de treino e de teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)

"""
Criando IA (usando Regressão Linear, RandomForest)

importar modelo
criar IA
treinar IA
"""
#criando modelos da IA
modelo_regressaoLinear = LinearRegression()
modelo_arvoreDecisao = RandomForestRegressor()

#treinando a IA
modelo_regressaoLinear.fit(x_treino, y_treino)
modelo_arvoreDecisao.fit(x_treino, y_treino)

#testando IA
previsao_regressaoLinear = modelo_regressaoLinear.predict(x_teste)
previsao_arvoreDecisao = modelo_arvoreDecisao.predict(x_teste)

# print(r2_score(y_teste, previsao_regressaoLinear))
# print(r2_score(y_teste, previsao_arvoreDecisao))


# #visualização das previsões
# tabela_auxiliar = pd.DataFrame()
# tabela_auxiliar['y_teste'] = y_teste
# tabela_auxiliar['Previsão Árvore Decisão'] = previsao_arvoreDecisao
# tabela_auxiliar['Previsão Regressão Linear'] = previsao_regressaoLinear
#
# sns.lineplot(data=tabela_auxiliar)
# plt.show()


#novas previsões

nova_tabela = pd.read_csv('novos.csv')

previsao = modelo_arvoreDecisao.predict(nova_tabela)

print(previsao)