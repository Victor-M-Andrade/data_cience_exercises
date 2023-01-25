"""
Automação Web e Busca de Informações com Python
Desafio:
Trabalhamos em uma importadora e o preço dos nossos produtos é vinculado a cotação de:

Dólar
Euro
Ouro
Precisamos pegar na internet, de forma automática, a cotação desses 3 itens
 e saber quanto devemos cobrar pelos nossos produtos, considerando uma margem de contribuição que temos na nossa base de dados.

Base de Dados: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv?usp=sharing
"""

"""
Importar cotações:
    Dolar
    Euro
    Ouro

Importar base de dados e atualizar a base
Recalcular os preços
Exportar base atualizada
"""

from os import system

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pandas as pd
import numpy as np

driver = webdriver.Chrome()

#Cotação Dólar
driver.get(('https://www.google.com/'))
driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Cotação Dolar')
driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = driver.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

#Cotação Euro
driver.get(('https://www.google.com/'))
driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Cotação Euro')
driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = driver.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

#Cotação Ouro
driver.get(('https://www.melhorcambio.com/ouro-hoje'))
cotacao_ouro = driver.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',','.')

# print(f'Cotação Dólar: {cotacao_dolar}')
# print(f'Cotação Euro: {cotacao_euro}')
# print(f'Cotação Ouro: {cotacao_ouro}')


#Importando base de dados
tabela = pd.read_excel('Produtos.xlsx', engine='openpyxl')


#Atualizando cotação na base de dados
tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(cotacao_dolar)
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(cotacao_euro)
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(cotacao_ouro)


#Atualizando preço de compra (cotação * preço original
tabela['Preço de Compra'] = tabela['Cotação'] * tabela['Preço Original']


#Atualizando preço de venda (preço de compra * margem
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']


#Exportar a base de dados
tabela.to_excel('Produtos_atualizados.xlsx', index=False)
print(tabela['Preço de Venda'])