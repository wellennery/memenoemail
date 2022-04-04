#Instalação das bibliotecas
#!pip install pyautogui
#!pip install pyperclip
# novo comentario 2
import pyautogui as pa
import pyperclip as pc
import time

pa.PAUSE = 1

# 1 - Abrir o outlook e novo e-mail
pa.press("win")
pa.write("outlook")
pa.press("enter")
time.sleep(3)
pa.click(x=26, y=104)

# 2 - Endereçar à Vi com assunto "deu bom"
time.sleep(2)
pa.write("email@gmail.com")
pa.press("tab")
pa.press("tab")
pa.press("tab")
pa.write("Deu bom")


# 3 - Escrever corpo do e-mail
pa.press("tab")
texto = """
Prezado(a), boa noite!

Tenho um meme especialmente para você:"""

pc.copy(texto)
pa.hotkey("ctrl", "v")

# 4 - Entrar na imagem para tirar um print
pa.press("win")
pa.write("chrome")
pa.press("enter")
time.sleep(2)
pa.write("https://i.pinimg.com/564x/b0/2e/e3/b02ee3623cf650913206a3b05fc1b3d7.jpg")
pa.press("enter")

# 5 - Tirar um print
time.sleep(1)
pa.hotkey("ctrl", "PrtSc")
pa.hotkey("alt", "tab")

# 6 - Colar imagem no corpo do e-mail
pa.hotkey("ctrl", "v")
pa.press("enter")
texto = """

Um beijo!!

"""

pc.copy(texto)
pa.hotkey("ctrl", "v")

# 7 - Enviar o e-mail
pa.click(x=60, y=209)
