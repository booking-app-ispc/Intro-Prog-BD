import pyodbc
from models.usuario import Usuario
from services.database_service import get_connection

def list_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT Id, Nombre, Usuario, Rol FROM Usuarios')
    users = cursor.fetchall()
    print("\n Lista de usuarios:")
    for u in users:
        print(Usuario(*u))
    cursor.close()
    conn.close()

def delete_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Usuarios WHERE Id = ?', (int(user_id),))
    conn.commit()
    print(" Usuario eliminado." if cursor.rowcount > 0 else " Usuario no encontrado.")
    cursor.close()
    conn.close()

def update_user_role(user_id, new_role):
    if new_role not in ["admin", "usuario"]:
        print(" Rol inválido.")
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE Usuarios SET Rol = ? WHERE Id = ?', (new_role, int(user_id)))
    conn.commit()
    print(" Rol actualizado." if cursor.rowcount > 0 else " Usuario no encontrado.")
    cursor.close()
    conn.close()

def get_user_by_credentials(username, hashed_password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT Id, Nombre, Usuario, Rol FROM Usuarios WHERE Usuario = ? AND Contrasena = ?''',
                   (username, hashed_password))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return Usuario(*row) if row else None

def add_user_to_db(nombre, usuario, hashed_password, rol):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Usuarios (Nombre, Usuario, Contrasena, Rol) VALUES (?, ?, ?, ?)''',
                   (nombre, usuario, hashed_password, rol))
    conn.commit()
    cursor.close()
    conn.close()