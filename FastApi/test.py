import mysql.connector
import os

# Configuración de la base de datos
db_config = {
    'user': '3RdETPb7WtnLHoN.root',
    'password': 'D46R3OHY0w3tWdpg',
    'host': 'gateway01.us-east-1.prod.aws.tidbcloud.com',
    'port': 4000,
    'database': 'test'
}

# Intentar conectarse a la base de datos
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    # Ejecutar una consulta de prueba
    cursor.execute("SELECT 1")
    result = cursor.fetchone()

    print("Conexión exitosa a la base de datos. Resultado de la consulta: ", result)

except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos: {err}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Conexión cerrada.")
    else:
        print("No se pudo cerrar la conexión a la base de datos porque no estaba abierta.")
