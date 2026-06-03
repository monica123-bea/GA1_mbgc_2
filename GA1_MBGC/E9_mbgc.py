# MÓNICA GARCÍA
# EJERCICIOS DE LISTAS

from colorama import init, Fore, Back, Style

import pyfiglet

titulo = pyfiglet.figlet_format("MONICA")
print(Fore.CYAN + titulo + Style.RESET_ALL)
init()
print(Fore.MAGENTA + "")

temperaturas = []
# Ciclo para capturar datos de 5 días
for indice in range(1,6):
    temperatura = []
    # Pide y agrega la temperatura máxima del día actual
    temperatura.append(int(input("🌡️ Día %d. Temperatura máxima: " % indice)))
    # Pide y agrega la temperatura mínima del día actual
    temperatura.append(int(input("❄️ Día %d. Temperatura mínima: " % indice)))
    # Guarda la sublista del día en la lista principal
    temperaturas.append(temperatura)
# Mostrar temperatura media
print("📊 Temperaturas medias")
print("====================")
indice = 1
# Recorre cada sublista de temperaturas
for temperatura in temperaturas:
    # Calcula el promedio entre máxima y mínima y lo muestra
    print("📈 Día %d. Temperatura media: %f" % (indice,sum(temperatura)/len(temperatura)))
    indice += 1
# Calcular temperatura mínima más pequeña
# Supongo que es la primera
temp_min = temperaturas[0][1]
# Recorre la lista para buscar una menor
for temperatura in temperaturas:
    # Si encuentra una mínima más baja, actualiza la variable
    if temperatura[1] < temp_min:
        temp_min = temperatura[1]
# Mostrar los días con menos temperatura
print("📉 Días con menos temperatura")
print("=============================")
indice = 1
# Busca qué días coinciden con la mínima más baja
for temperatura in temperaturas:
    # Si la mínima del día es igual a la mínima global
    if temperatura[1] == temp_min:
        # Muestra el número de día
        print("📍 Día %d" % indice)
    indice += 1
# Días con temperatura máxima
existe_temperatura = False
print("🔥 Días con temperatura máxima")
print("==============================")
# Solicita un valor de temperatura al usuario
temp_max = int(input("🔍 Introduce una temperatura: "))
indice = 1
# Recorre la lista buscando coincidencias con la máxima
for temperatura in temperaturas:
    # Si la temperatura máxima del día coincide con la buscada
    if temperatura[0] == temp_max:
        # Muestra el día encontrado
        print("🎯 Día %d" % indice)
        existe_temperatura = True
    indice += 1
# Si no se encontró ninguna coincidencia en el ciclo
if not existe_temperatura:
    # Muestra un mensaje de aviso
    print("❌ No hay ningún día con dicha temperatura.")