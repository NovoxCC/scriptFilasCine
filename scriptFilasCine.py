import string
import mysql.connector

# Configuración de la conexión a la base de datos
config = {
    'user': 'root',
    'password': '123456789',
    'host': 'localhost',
    'database': 'pos_cinema',
}

# Filas deseadas
filas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

# Asientos por fila
asientos_por_fila = 20

# Tipo y costo según la fila
tipo_general = 'General'
costo_general = 8000

tipo_preferencial = 'Preferencial'
costo_preferencial = 11000

# Crear la conexión
conn = mysql.connector.connect(**config)

# Crear un cursor
cursor = conn.cursor()

# Iterar sobre las filas y ejecutar las consultas de inserción
for fila in filas:
    tipo = tipo_preferencial if fila in ('I', 'J', 'K') else tipo_general
    costo = costo_preferencial if fila in ('I', 'J', 'K') else costo_general

    consulta = f"INSERT INTO Seats (row_letter, seat_number, type, status, cost) VALUES "
    valores = ", ".join([f"('{fila}', {asiento}, '{tipo}', 'Disponible', {costo})" for asiento in range(1, asientos_por_fila + 1)])
    consulta += valores

    # Ejecutar la consulta
    cursor.execute(consulta)

# Confirmar la transacción
conn.commit()

# Cerrar el cursor y la conexión
cursor.close()
conn.close()
