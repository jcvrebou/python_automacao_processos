# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:07:59 2023

@author: Jean
IDE: Spyder
"""

# Instalação de bibliotecas

# pip install PyAutoGUI
# pip install pandas
#pip freeze > requirements.txt # Arquivo com todas as dependências instaladas no projeto

# Importação de bibliotecas
import pyautogui
import time
import pandas as pd
  
pyautogui.PAUSE = 1 # Pausa entre a execução de cada comando do pyautogui

# Passo 1: Abrir o sistema
    
    # Abrir o iniciar do sistema operacional
pyautogui.press("win")

    # Digitar o nome do navegador na pesquisa
pyautogui.write("chrome")

    # Abrir o navegador
pyautogui.press("enter")

    # Acessar o site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

    # Aguardar o carregamento do site
time.sleep(2)


# Passo 2: Fazer login no sistema

    # Verificar posição do mouse no campo login
#print(pyautogui.position())

    # Digitar email no campo usuário
pyautogui.click(x = 261, y = 436)
email = "usertreinamento@gmail.com"
pyautogui.write(email)

    # Aguardar após o preenchimento do login
time.sleep(3)

    # Passar para o campo de senha
pyautogui.press("tab")

    # Digitar senha
senha = "Treinamento"
pyautogui.write(senha)

    # Aguardar após o preenchimento da senha e efetuar login
time.sleep(3)
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importar a base de dados
tabela = pd.read_csv('produtos.csv')


# Passo 4: Cadastrar 1 produto como teste

    # Inserir posição do 1º campo do cadastro
pyautogui.click(x = 536, y = 307)

    # Preencher os campos
pyautogui.write("Codigo")
pyautogui.press("tab")
pyautogui.write("Marca")
pyautogui.press("tab")
pyautogui.write("Tipo")
pyautogui.press("tab")
pyautogui.write("Categoria")
pyautogui.press("tab")
pyautogui.write("Preco")
pyautogui.press("tab")
pyautogui.write("Custo")
pyautogui.press("tab")
pyautogui.write("Obs")

    # Tab para ir para o botão enviar e aplicar o enter
pyautogui.press("tab")
pyautogui.press("enter")

pyautogui.scroll(7000)

# Passo 5: Repetir o cadastro para todos os produtos

for linha in tabela.index: # para cada item na tabela
    
    pyautogui.click(x = 536, y = 307) # Inserir posição do 1º campo do cadastro
    
    # variáveis para indicar as colunas onde os dados devem ser coletados
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]
    
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    
    if not pd.isna(obs):
            
            pyautogui.write(str(obs))
    
        # Tab para ir para o botão enviar e aplicar o enter
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(7000)