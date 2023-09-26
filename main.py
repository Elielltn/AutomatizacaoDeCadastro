import time
import pyautogui

pyautogui.PAUSE = 0.3

# abrir chrome
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
time.sleep(3)

# fazer login
pyautogui.click(x=836, y=362)
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# importar base de dados com pandas
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# cadastrar o produto 
for linha in tabela.index:
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    precoUnit = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]
    pyautogui.click(x=872, y=241)
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(precoUnit))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    # Pressionar Enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(50000)