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
from os import system

df = pd.read_csv('telecom_users.csv')



#Eliminar coluna 'Unnamed: 0'
df = df.drop('Unnamed: 0', axis=1)

#Resolver valores sendo reconhecidos errados (usar df.info() para analisar)
df['TotalGasto'] = pd.to_numeric(df['TotalGasto'], errors='coerce')

#resolver valores vazios

#colunas em que TODAS('all') as linhas sao NaN eu vou excluir
df = df.dropna(how='all', axis=1)

#excluir linhas que tem PELO MENOS('any') 1 valor vazio (NaN)
df = df.dropna(how='any', axis=0)

def analiseInicial():
    print(df['Churn'].value_counts())
    print('-'*30)
    print(df['Churn'].value_counts(normalize=True).map('{:.2%}'.format))
    system('pause')

def analiseDetalhada():
    for coluna in df.columns:
        grafico = px.histogram(df, x=coluna, color='Churn', text_auto=True)
        grafico.show()


def menu():
    global df
    while True:
        system('cls')
        print('*'*80)
        print('Análise de Usuários'.center(80, ' '))
        print('*'*80)

        print('1 - Mostrar informações dos dados')
        print('2 - Análise Inicial')
        print('3 - Análise Detalhada')
        print('OBS: Para sair digite qualquer valor')


    
        try:
            opcao = int(input('Digite uma opção: '))

            if opcao == 1:
                print('')
                print(df.info())
                system('pause')
            elif opcao == 2:
                print('')
                analiseInicial()
                print('')
            elif opcao == 3:
                analiseDetalhada()
            else:
                print('\nSaindo.....')
                break
        except:
            print('\nSaindo.....')
            break

menu()