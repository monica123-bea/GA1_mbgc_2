# MÓNICA GARCÍA
# EJERCICIOS DE LISTAS

from colorama import init, Fore, Back, Style

import pyfiglet

titulo = pyfiglet.figlet_format("MONICA")
print(Fore.CYAN + titulo + Style.RESET_ALL)
init()
print(Fore.MAGENTA + "")

import random
# Lista vacía para almacenar números
lista = []
# Ciclo para generar 10 números
for indice in range(1,11):
    # Agrega un número aleatorio entre 1 y 10
    lista.append(random.randint(1,10))
# Ordeno la lista
lista.sort()

# Recorro el vector ordenado
for numero in lista:
    # Imprime cada número con espacio en una línea
    print("🔢", numero," ", end="")