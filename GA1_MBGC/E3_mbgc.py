# MÓNICA GARCÍA
# EJERCICIOS DE LISTAS

from colorama import init, Fore, Back, Style

import pyfiglet

titulo = pyfiglet.figlet_format("MONICA")
print(Fore.CYAN + titulo + Style.RESET_ALL)
init()
print(Fore.MAGENTA + "")

# Lista vacía para las calificaciones
notas = []
# Ciclo para solicitar 5 notas
for indice in range(1,6):
    # Bucle infinito para validar la nota
    while True:
        # Pide la nota por teclado
        nota = int(input("📝 Introduce la nota %d: " % indice))
        # Verifica que esté entre 0 y 100
        if nota>=0 and nota<=100: break
    # Agrega la nota validada a la lista
    notas.append(nota)
# Muestra la etiqueta de notas sin salto de línea
print("📊 Notas: ", end="")
# Recorremos la lista de notas
for nota in notas:
    # Imprime cada nota con un espacio
    print(nota, " ", end="")
# Genera un salto de línea
print()
# Calcula y muestra el promedio
print("🧮 Nota media: ", sum(notas)/len(notas))
# Encuentra y muestra la nota más alta
print("🏆 Nota max: ", max(notas))
# Encuentra y muestra la nota más baja
print("📉 Nota min: ", min(notas))
