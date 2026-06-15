# Mónica García
# El archivo conexion.py
from conexion import obtener_conexion

# Define una funcion para mostrar los libros registrados
def mostrar_libros():

    # Crea una conexion con la base de datos
    conexion = obtener_conexion()
    # Crea un cursor para ejecutar las intrucciones de SQL
    cursor = conexion.cursor()
    #Ejecuta una consula de SQL para obtener el id y nombre
    # de todos los llibros registrados en la base de datos
    cursor.execute("SELECT id, nombre FROM libros")
    # Guarda todods los resultados de la consulta
    # en la variable libros
    libros = cursor.fetchall()
    # Verifica si la lista de libros esta vacio
    if len(libros) == 0:
        # Muestra mensaje si no hay libros registrados
        print("\n No hay libros registrados. \n")
    # Si hay libros registrados
    else:
        # Muestra ek titulo del catalogo
        print("\n ===== CATALOGO DE LIBROS =====")
        # Recorre cada libro obtenido desde la base de datos
        for libro in libros:
            # Muestra el id y el nombre del libro
            print(f"{libro[0]}. {libro[1]}")
            # Imprimio una linea en blanco
            print()

        cursor.close()
        conexion.close()

#----------------------------------------------------------------------------------
# Define uan función para agregar libros
def agregar_libro():

    # Crea una conexion con la base de datos
    conexion = obtener_conexion()
    # Crea un cursor para ejecutar las instrucciones de SQL
    cursor = conexion.cursor()
    # Solicita al usuario el nombre del libro y elimina espacion innecesarios
    libro = input("Ingrese el nombre del libro: ").strip()
    # Verirfica si el usuario escribio algo
    if libro:
        # Prepara la consulta de SQL para insertar un libro
        sql = "INSERT INTO libros (nombre) VALUES (%s)"
        # Guarda el nombre del libro en un tupla
        valores = (libro,)
        # Ejecuta la consulta SQL con el valor ingresado
        cursor.execute(sql, valores)
        # Guarda definitivamente el cambio en la base de datos
        conexion.commit()
        # Muestra mensaje de confirmación
        print(f"\n✅ libro '{libro}' Agregado correctamente.\n")
    # Si el usuario no escribió nada
    else:
          # Muestra advertencia
          print("⚠️No puede ingresar un libro vacio.\n")
    # Cierra el cursor
    cursor.close()
    # Cierra la conexion con la base de datos
    conexion.close()

#----------------------------------------------------------------------------------
# Define una función para eliminar libros
def eliminar_libro():

    # Crea una conexión con la base de datos
    conexion = obtener_conexion()
    # Crea un cursor para ejecutar instrucciones SQL
    cursor = conexion.cursor()
    # Solicita el nombre del libro que se desea eliminar
    libro = input("Ingrese el nombre del libro a eliminar: ").strip()
    # Prepara la consulta SQL para eliminar el libro por nombre
    sql = "DELETE FROM libros WHERE nombre = %s"
    # Guarda el nombre del libro en una tupla
    valores = (libro,)
    # Ejecuta la consulta SQL
    cursor.execute(sql, valores)
    # Guarda definitivamente el cambio en la base de datos
    conexion.commit()
    # Verifica si se eliminó al menos un registro
    if cursor.rowcount > 0:
        # Muestra mensaje si el libro fue eliminado
        print(f"\n🗑 Libro '{libro}' eliminado correctamente.\n")
    # Si no se eliminó ningún registro
    else:
        # Muestra mensaje indicando que el libro no existe
        print(f"\n⚠ El libro '{libro}' no existe.\n")
    # Cierra el cursor
    cursor.close()
    # Cierra la conexión con la base de datos
    conexion.close()

# ----------------------------------------------------------------------------------
# Define el menú para el administrador
def menu_administrador():

    # Inicia un bucle para mostrar el menú repetidamente
    while True:
        # Muestra el título del menú administrador
        print("===== MENÚ ADMINISTRADOR =====")
        # Muestra la opción para agregar libros
        print("1. Agregar un libro")
        # Muestra la opción para eliminar libros
        print("2. Eliminar un libro")
        # Muestra la opción para mostrar libros
        print("3. Mostrar catálogo de libros")
        # Muestra la opción para salir
        print("4. Salir")
        # Solicita al usuario una opción
        opcion = input("Seleccione una opción: ")
        # Si el usuario elige la opción 1
        if opcion == "1":
            # Llama a la función agregar_libro
            agregar_libro()
        # Si el usuario elige la opción 2
        elif opcion == "2":
            # Llama a la función eliminar_libro
            eliminar_libro()
        # Si el usuario elige la opción 3
        elif opcion == "3":
            # Llama a la función mostrar_libros
            mostrar_libros()
        # Si el usuario elige la opción 4
        elif opcion == "4":
            # Muestra mensaje de despedida
            print("\n👋 Gracias por usar el sistema.")
            # Rompe el bucle y sale del menú
            break
        # Si el usuario escribe una opción incorrecta
        else:
            # Muestra mensaje de error
            print("\n❌ Opción inválida.\n")

# ----------------------------------------------------------------------------------
# Define el menú para el usuario normal
def menu_usuario():

    # Inicia un bucle para mostrar el menú repetidamente
    while True:
        # Muestra el título del menú usuario
        print("===== MENÚ USUARIO =====")
        # Muestra la opción para ver libros
        print("1. Mostrar catálogo de libros")
        # Muestra la opción para salir
        print("2. Salir")
        # Solicita al usuario una opción
        opcion = input("Seleccione una opción: ")
        # Si el usuario elige la opción 1
        if opcion == "1":
            # Llama a la función mostrar_libros
            mostrar_libros()
        # Si el usuario elige la opción 2
        elif opcion == "2":
            # Muestra mensaje de despedida
            print("\n👋 Gracias por usar el sistema.")
            # Rompe el bucle y sale del menú
            break
        # Si el usuario escribe una opción incorrecta
        else:
            # Muestra mensaje de error
            print("\n❌ Opción inválida.\n")