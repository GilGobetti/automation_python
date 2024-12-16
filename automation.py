# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

import pyautogui
import time

pyautogui.PAUSE = 0.3
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=418, y=403)
pyautogui.write("python@curso.com")
pyautogui.press("tab")
pyautogui.write("12345")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.click(x=421, y=290)

import pandas

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write (str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write (str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write (str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write (str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write (str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write (str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.scroll(5000)
    time.sleep(1)
    pyautogui.click(x=421, y=290)
    

#print(tabela)
