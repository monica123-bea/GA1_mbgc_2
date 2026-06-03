# MÓNICA GARCÍA
# EJERCICIOS DE LISTAS

from colorama import init, Fore, Back, Style

import pyfiglet

titulo = pyfiglet.figlet_format("MONICA")
print(Fore.CYAN + titulo + Style.RESET_ALL)
init()
print(Fore.MAGENTA + "")

# Listas vacías para nombres y edades
nombres = []
edades = []
# Inicializo las listas hasta que introduzca un "*"
while True:
    # Solicita el nombre del alumno
    nombre = input("👤 Dime el nombre de un alumno: ")
    # Si no es un asterisco guarda los datos
    if nombre != "*":
        # Agrega el nombre a su lista
        nombres.append(nombre)
        # Pide y agrega la edad como entero
        edades.append(int(input("🎂 Dime su edad: ")))
    # Si es un asterisco sale del bucle
    if nombre == "*": break;
# Calcular la edad máxima
edad_max = max(edades)
# Alumnos mayores de edad
print("🧑 Alumnos mayores de edad")
print("=======================")

# Recorre ambas listas al mismo tiempo
for nombre,edad in zip(nombres,edades):
    # Filtra si es mayor o igual a 18
    if edad >= 18:
        # Muestra el nombre
        print("🔹", nombre)
# Alumnos mayores
print("👑 Alumnos mayores")
print("===============")
# Recorre ambas listas de nuevo
for nombre,edad in zip(nombres,edades):
    # Filtra a los que tienen la edad máxima
    if edad == edad_max:
        # Muestra el nombre
        print("⭐", nombre)