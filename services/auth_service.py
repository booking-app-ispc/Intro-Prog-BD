import hashlib
import re
from repository.user_repository import get_user_by_credentials, add_user_to_db

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_password(password):
    return len(password) >= 6 and re.search(r"[a-zA-Z]", password) and re.search(r"\d", password)

def login_user(username, password):
    return get_user_by_credentials(username.strip(), hash_password(password))

def register_user():
    nombre = input("Nombre completo: ")
    usuario = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    rol = input("Rol (admin/usuario): ").lower()

    if not nombre.strip() or not usuario.strip():
        print(" El nombre y el usuario no pueden estar vacíos.")
        return

    if rol not in ["admin", "usuario"]:
        print(" Rol inválido.")
        return

    if not is_valid_password(password):
        print(" La contraseña debe tener al menos 6 caracteres, incluyendo letras y números.")
        return

    try:
        add_user_to_db(nombre.strip(), usuario.strip(), hash_password(password), rol)
        print(" Usuario registrado con éxito.")
    except Exception as e:
        print(f" Error: {e}")
