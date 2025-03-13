import yfinance
import pyautogui
import pyperclip
import webbrowser
import time
import datetime

# Recolectar datos de las acciones
cod_accion = input("Ingrese el codigo de la accion: ")

fecha_ini = input("Ingrese la fecha de inicio con este formato DD/MM/YYYY: ")
fecha_fin = input("Ingrese la fecha de fin del periodo solicitado con este formato DD/MM/YYYY: ")

fecha_inicio_datetime = datetime.datetime.strptime(fecha_ini,"%d/%m/%Y")
fecha_fin_datetime = datetime.datetime.strptime(fecha_fin, "%d/%m/%Y")

datos = yfinance.Ticker(cod_accion).history(start=fecha_inicio_datetime,end=fecha_fin_datetime)
datos_cierre = datos.Close

min = round(datos_cierre.min(),2)
max = round(datos_cierre.max(),2)
media = round(datos_cierre.mean(),2)

# Parte del envio de los datos por e-mail

email = "fioravanti.vivi@gmail.com"

asunto = input("Ingrese el asunto del correo: ")

mensaje = f"""
Estimado Administrador,

a continuación adjunto los datos del análisis solicitado de la acción: {cod_accion}

Cotización máxima: ${max}
Cotización mínima: ${min}
Cotización media: ${media}

Cualquier consulta, no dude en avisarme.

Saludos,
Vivian
"""

webbrowser.open("www.gmail.com")
time.sleep(3)

pyautogui.PAUSE = 3

pyautogui.click(x=85, y=172)

pyperclip.copy(email)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

pyperclip.copy(asunto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

pyperclip.copy(mensaje)
pyautogui.hotkey("ctrl","v")

pyautogui.click(x=1295, y=1006)

pyautogui.hotkey("ctrl","f4")

