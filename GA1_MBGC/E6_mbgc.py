# MÓNICA GARCÍA
# EJERCICIOS DE LISTAS

from colorama import init, Fore, Back, Style

import pyfiglet

titulo = pyfiglet.figlet_format("MONICA")
print(Fore.CYAN + titulo + Style.RESET_ALL)
init()
print(Fore.MAGENTA + "")

# Lista con los días de cada mes
dias = [31,28,31,30,31,30,31,31,30,31,30,31]
# Lista con los nombres de los meses
nombre_mes = ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
              "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
# Bucle infinito para validar entrada
while True:
    # Solicita el número de mes al usuario
    mes = int(input("📅 Introduce un mes (1-12): "))
    # Verifica si el rango es inválido
    if mes < 1 or mes > 12:
        # Muestra mensaje de error
        print("❌ Error: mes incorrecto.")
    # Si el mes es válido rompe el bucle
    if mes>=1 and mes<=12: break
# Imprime el resultado final combinando las listas
print("🗓️ El mes de", nombre_mes[mes-1], "tiene", dias[mes-1], "días.")