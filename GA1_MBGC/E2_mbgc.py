# MÓNICA GARCÍA
# EJERCICIOS DE LISTAS

from colorama import init, Fore, Back, Style

import pyfiglet

titulo = pyfiglet.figlet_format("MONICA")
print(Fore.CYAN + titulo + Style.RESET_ALL)
init()
print(Fore.MAGENTA + "")

# Listas para almacenar los datos
lista1 = []
lista2 = []
# Ciclo para pedir 5 cadenas
for indice in range(1,6):
    # Guarda la cadena ingresada por el usuario
    lista1.append(input("✍️ Dame la cadena %d: " % indice))
# Invierte la lista original
lista2 = lista1[::-1]
# Recorre la lista invertida
for cadena in lista2:
    # Imprime cada cadena en pantalla
    print("📋", cadena)