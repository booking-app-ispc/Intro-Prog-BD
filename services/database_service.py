import pyodbc

def check_database():
    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=localhost\\SQLEXPRESS;Database=master;Trusted_Connection=yes;Encrypt=yes;TrustServerCertificate=yes;", autocommit=True)
    cursor = conn.cursor()
    cursor.execute("IF DB_ID('crudUsers') IS NULL BEGIN CREATE DATABASE crudUsers END")
    cursor.close()
    conn.close()

def get_connection():
    return pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=localhost\\SQLEXPRESS;Database=crudUsers;Trusted_Connection=yes;Encrypt=yes;TrustServerCertificate=yes;")

def create_user_table():
    conn = get_connection()
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