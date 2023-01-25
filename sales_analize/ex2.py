"""
Colunas:

home: indica se o usuário acessou ou não a página inicial.
how_it_works: indica se o usuário acessou ou não a página de “Como funciona a Empresa”.
contact: indica se o usuário acessou ou não a página de contato da empresa.
bought: indica se o usuário efetuou uma compra ou não.

Indetifique e extraia informações desses dados em formas de gráficos

BONUS: faça uso de IA para gerar previsões de vendas

"""

import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from os import system

def analise_pandas(dados):
    print(dados)
    print(dados.info())

def heatmap(dados):
    correlacao_dados = dados.corr()

    grafico = px.imshow(correlacao_dados, labels=dict(y='Página acessada', color='Efetividade'),
                        color_continuous_scale=px.colors.sequential.Greens, text_auto=True)


    grafico.update_layout(title={
        'text': 'CORRELAÇÃO ENTRE VENDAS E PÁGINAS ACESSADAS',
        'x': 0.5
    })

    grafico.show()


def histogram(dados):
    colunas = ['home', 'how_it_works', 'contact']
    for coluna in colunas:
        grafico = px.histogram(dados, x=coluna, color='bought', text_auto=True)
        grafico.update_layout(bargap=0.2)
        grafico.show()

def bars(dados):
    dados = dados[dados['bought'] == 1]
    valores = dados.sum()
    indices = [['home',valores['home']], ['how_it_works',valores['how_it_works']], ['contact',valores['contact']]]
    df_auxiliar = pd.DataFrame(indices, columns=['pagina', 'qtd'])

    grafico = px.bar(df_auxiliar, x='pagina', y='qtd', labels={
        'pagina':'Páginas Acessadas',
        'qtd':'Quantiidade de Acessos'}, color_discrete_sequence=px.colors.qualitative.T10, text_auto=True)

    grafico.update_layout(title={
        'text' : 'PÁGINAS QUE MAIS GERARAM VENDAS',
        'x': 0.5
    })
    grafico.show()

def colors():
    colors = px.colors.qualitative.swatches()
    colors.show()




def previsao(dados):
    y = dados['bought'] #quem eu quero prever
    x = dados[['home', 'how_it_works', 'contact']] #quem sera analisado

    x = x.values # apenas para retirar o aviso

    # dividr base de treino e de teste
    x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)

    # criando modelos da IA
    modelo_arvoreDecisao = RandomForestRegressor()

    # treinando a IA
    modelo_arvoreDecisao.fit(x_treino, y_treino)

    # testando IA
    previsao_arvoreDecisao = modelo_arvoreDecisao.predict(x_teste)

    home = int(input("Acessou a home? "))
    how_it_works = int(input("Acessou a how_it_works? "))
    contact = int(input("Acessou a contact? "))

    previsao = modelo_arvoreDecisao.predict([[home, how_it_works, contact]])

    print(f'A probabilidade de gerar venda é de: {float(previsao):,.4%}')
    print(f'A IA possui acertibilidade de {r2_score(y_teste, previsao_arvoreDecisao):,.4%}')


def menu():
    global dados
    while True:
        system('cls')
        divisor = '*'*70
        print(divisor)
        print('Análise de páginas que geram vendas')
        print(divisor)

        print('1 - Base de Dados a ser analisada')
        print('2 - Gráfico de Mapa de Calor')
        print('3 - Gráfico de Histograma')
        print('4 - Gráfico de Barras')
        print('5 - Previsão de possível venda')
        print('6 - Sair\n')

        try:
            opcao = int(input('Digite uma opção: '))

            match opcao:
                case 1:
                    analise_pandas(dados)
                    system('pause')
                case 2:
                    heatmap(dados)
                    system('pause')
                case 3:
                    histogram(dados)
                    system('pause')
                case 4:
                    bars(dados)
                    system('pause')
                case 5:
                    previsao(dados)
                    system('pause')
                case 6:
                    print('Saindo.....')
                    system('pause')
                    break
        except:
            print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')
            system('pause')


dados = pd.read_csv('tracking.csv')

menu()

