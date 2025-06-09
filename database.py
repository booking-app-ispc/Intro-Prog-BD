import pyodbc
import re
import hashlib

def check_database():
    try:
        conn = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=localhost\\SQLEXPRESS;"
            "Database=master;"
            "Trusted_Connection=yes;"
            "Encrypt=yes;"
            "TrustServerCertificate=yes;",
            autocommit=True
        )
        cursor = conn.cursor()
        cursor.execute("IF DB_ID('crudUsers') IS NULL BEGIN CREATE DATABASE crudUsers END")
        print(" Base de datos verificada o creada.")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f" Error al crear/verificar base de datos: {e}")

def get_connection():
    try:
        return pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=localhost\\SQLEXPRESS;"
            "Database=crudUsers;"
            "Trusted_Connection=yes;"
            "Encrypt=yes;"
            "TrustServerCertificate=yes;"
        )
    except Exception as e:
        print(f" Error de conexión: {e}")
        return None

def create_user_table():
    conn = get_connection()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute('''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Usuarios' AND xtype='U')
        CREATE TABLE Usuarios (
            Id INT PRIMARY KEY IDENTITY,
            Nombre NVARCHAR(100),
            Usuario NVARCHAR(50) UNIQUE,
            Contrasena NVARCHAR(100),
            Rol NVARCHAR(20)
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_password(password):
    return len(password) >= 6 and re.search(r"[a-zA-Z]", password) and re.search(r"\d", password)