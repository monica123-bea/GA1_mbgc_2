# MÓNICA GARCÍA
# EJERCICIOS DE LISTAS

from colorama import init, Fore, Back, Style

import pyfiglet

titulo = pyfiglet.figlet_format("MONICA")
print(Fore.CYAN + titulo + Style.RESET_ALL)
init()
print(Fore.MAGENTA + "")

# Lista vacía para el vector
lista = []
# Pide el primer número entero
numero = int(input("📥 Introduce un número en la lista: "))
# Ciclo que frena si el número es negativo
while numero>=0:
    # Añade el número positivo a la lista
    lista.append(numero)
    # Solicita el siguiente número
    numero = int(input("🔄 Introduce un número en la lista: "))

# Recorre la lista final
for numero in lista:
    # Imprime los elementos en una sola línea
    print("✅", numero," ", end="")