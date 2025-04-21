#data base, para la conexion a mysql

import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="AVC123Wsa",
        database="clinicadental"
    )
