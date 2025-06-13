from services.database_service import check_database, create_user_table
from services.auth_service import login_user, register_user
from repository.user_repository import list_users, delete_user_by_id, update_user_role
from models.usuario import Usuario

def admin_menu():
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Ver usuarios")
        print("2. Eliminar usuario")
        print("3. Modificar rol de un usuario")
        print("0. Cerrar sesión")
        option = input("Opción: ")
        if option == "1":
            list_users()
        elif option == "2":
            user_id = input("ID del usuario a eliminar: ")
            delete_user_by_id(user_id)
        elif option == "3":
            user_id = input("ID del usuario: ")
            new_role = input("Nuevo rol (admin/usuario): ").lower()
            update_user_role(user_id, new_role)
        elif option == "0":
            break
        else:
            print(" Opción inválida.")

def user_menu(user: Usuario):
    print(f"\n Bienvenido/a {user.nombre}")
    print(f" Tu usuario: {user.usuario}")
    print(f" Tu rol: {user.rol}")
    input("Presiona ENTER para cerrar sesión.")

def main_menu():
    check_database()
    create_user_table()

    while True:
        print("\n=== Sistema de Gestión de Usuarios ===")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("0. Salir")
        option = input("Seleccione una opción: ")

        if option == "1":
            register_user()
        elif option == "2":
            username = input("Usuario: ")
            password = input("Contraseña: ")
            user = login_user(username, password)
            if user:
                if user.rol == "admin":
                    admin_menu()
                else:
                    user_menu(user)
            else:
                print("Usuario o contraseña incorrectos.")
        elif option == "0":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main_menu()