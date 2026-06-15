# Mónica García

# Importamos la libreria de mysql.conncector para
# conectar Python con MySQL
import mysql.connector

def obtener_conexion():
    # Crea la conexion con la base de datos MySQL
    conexion = mysql.connector.connect(
        # Indica el usuario de mysql
        host="localhost",
        # Indica el usuario de mysql
        user="root",
        # Indica la contraseña del usuario root de mysql
        password="123456789",
        # Indica el nombre de la base de datos que se va a utilizar
        database="biblioteca_db"
    )
    # Devuelve la conexion para poder usarla en los otros archivos
    return conexion