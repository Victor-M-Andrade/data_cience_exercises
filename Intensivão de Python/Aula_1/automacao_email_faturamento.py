"""
Passo 1: entrar no sistema da empresa link: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga (provisório)
Passo 2: navegar até o local do relatório (entrar na pasta Exportar)
Passo 3: Exportar o relatório (download)
Passo 4: Calcular os indicadfores (faturamento e quantidade de produtos)
Passo 5: Enviar um e-mail para a diretoria
"""

"""
pyautogui.click() click mouse
pyautogui.write() escrever algo
pyautogui.press() pressionar uma única tecla
pyautogui.hotkey() pressionar combinação de teclas
"""

import pyautogui as pa
import time
import pandas as pd
import openpyxl

link = 'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga'
pa.PAUSE = 1.5
pa.FAILSAFE = True

pa.press('win')
pa.write('chrome')
pa.press('enter')
pa.press('f6')
pa.write(link)
pa.press('enter')
pa.hotkey('ctrl', 'f')
pa.write('Exportar')
pa.hotkey('ctrl', 'enter')
pa.press('enter')
pa.moveTo(380, 308)
pa.click(button ='right')
pa.press('up')
pa.press('enter')


pa.press('f6')
pa.write('https://mail.google.com/')
pa.press('enter')
time.sleep(3)
pa.hotkey('ctrl', 'f')
pa.write('Escrever')
pa.hotkey('ctrl', 'enter')
pa.write('victorma2000@live.com')
pa.press('tab')
pa.press('tab')
pa.write('Faturamento Mensal')
pa.press('tab')

#calculo do faturamento
df = pd.read_excel(r"C:\Users\victo\Downloads\Vendas - Dez.xlsx", engine='openpyxl')

faturamento = df["Valor Final"].sum()
quantidade = df["Quantidade"].sum()

texto = f"""Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

Att.,
Victor Andrade
"""

pa.write(texto)
pa.press('tab')
pa.press('enter')

