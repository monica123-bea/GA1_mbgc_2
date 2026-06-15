# Mónica García

# Importa la funcion a obtener _conexion
# desde el archivo  conexion.py
from conexion import obtener_conexion

# Define una funcion llamada iniciar_sesion
def iniciar_sesion():
    # Crea una conexion con la base de datos
    conexion = obtener_conexion
    # Crea una variable llamada cursor para ejecutar instrucciones SQL
    cursor = conexion.cursor()
    print("==== INICIO DE SESION ====")

    # Inicia un bucle que se repita hasta que el
    #  usuario ingrese datos correctos
    while True:
        # Solicita el nombre de usuario
        usuario = input("Usuario: ")
        # Solicita la contraseña del usuario
        contraseña = input("Contraseña: ")
        # Consulta SQL que busca el rol del
        # usuario si el usuario y contraseña coinciden
        sql = "SELECT rol FROM usuarios where usuario = % AND contraseña =%s"
        # Guarda los valores que se envian a la consulta de SQL
        valores = (usuario, contraseña)
        # Ejecuta la consulta SQL  con los valores ingresados por el usuarios
        cursor.execute(sql, valores)
        # Obtiene un solo resultado de la consulta
        resultado = cursor.fetchone()
       # Verifica si se encontro un usuario valido
        if resultado:
            # Guarda el rol encontrado en la variable rol
            rol = resultado
            # Muestra un mensaje de bienvenida con el nombre del usuario
            print(f"\n Bienvenido {usuario}")
            # Muestra el rol del usuario
            print(f"\n Rol:  {rol}\n")
            # Cierra el cursor
            cursor.close
            # Cierra la conexion con la base de datos
            conexion.close
            # Devuelve el rol para que main.py sepa que meny mostrar
            return rol
        else:
            # Informa que los datos son incorrectos
            print("\n Usuario o Contraseña incorrecots. Intente Nuevamente. \n")