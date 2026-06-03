# MÓNICA GARCÍA
# EJERCICIOS DE LISTAS

from colorama import init, Fore, Back, Style

import pyfiglet

titulo = pyfiglet.figlet_format("MONICA")
print(Fore.CYAN + titulo + Style.RESET_ALL)
init()
print(Fore.MAGENTA + "")

import random
# Lista vacía para los números
lista_numeros = []

# Ciclo del 1 al 10
for indice in range(1,11):
    # Agrega un número aleatorio entre 1 y 10
    lista_numeros.append(random.randint(1,10))

# Recorre la lista para mostrar resultados
for numero in lista_numeros:
    # Imprime el número, su cuadrado y su cubo con emojis
    print("🎲", numero, " ⏩ ", numero ** 2, " ⏩ ", numero ** 3)