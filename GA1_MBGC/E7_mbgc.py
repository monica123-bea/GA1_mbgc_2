# MÓNICA GARCÍA
# EJERCICIOS DE LISTAS

from colorama import init, Fore, Back, Style

import pyfiglet

titulo = pyfiglet.figlet_format("MONICA")
print(Fore.CYAN + titulo + Style.RESET_ALL)
init()
print(Fore.MAGENTA + "")

# Inicializa tres listas vacías
lista1 = []
lista2 = []
lista3 = []
# Ciclo para llenar el primer vector
for indice in range(1,6):
    # Pide los datos numéricos del vector 1
    lista1.append(int(input("📥 Introduce el elemento %d del vector1: " % indice)))

# Ciclo para llenar el segundo vector
for indice in range(1,6):
    # Pide los datos numéricos del vector 2
    lista2.append(int(input("📥 Introduce el elemento %d del vector2: " % indice)))

# Ciclo para sumar posiciones iguales
for indice in range(0,5):
    # Guarda la suma en la tercera lista
    lista3.append(lista1[indice] + lista2[indice])

# Imprime la etiqueta de resultado
print("🧮 La suma de los vectores es:")
# Recorre la lista de resultados
for numero in lista3:
    # Muestra la suma de cada posición
    print("✅", numero, " ", end="")