# Intro-Prog-BD
Proyecto de Introducción a la Programación y Base de Datos

Integrantes: 

- Tomas Nicolas Nieto - Dni: 41481655 
- Evangelina Battauz - Dni: 35452615 
- García Virginia- Dni: 43367376


# Sistema de Gestión de Usuarios

Este proyecto es una aplicación simple en Python que permite registrar, iniciar sesión y administrar usuarios con distintos roles (admin o usuario). Utiliza una base de datos en SQL Server para almacenar los datos de los usuarios.

## 📁 Estructura del Proyecto

--main.py # Interfaz del programa (menú principal)

--models/usuario.py # Clase Usuario

--repository/usuario_repository.py # Acceso a base de datos (CRUD)

--services/usuario_service.py # Lógica del negocio (validaciones, operaciones)

--scripts/init_db.sql # Script SQL para crear la base de datos y tabla

--README.md # Este archivo


## ⚙️ ¿Qué hace el sistema?

- Crear usuarios con nombre, nombre de usuario, contraseña y rol.
- Iniciar sesión como usuario o admin.
- Ver lista de usuarios (admin).
- Eliminar usuarios (admin).
- Cambiar el rol de un usuario (admin).
- Ver datos personales (usuario).

## 🧠 Conceptos aplicados

- Programación orientada a objetos (clase `Usuario`)
- Principio de responsabilidad única (cada parte del código tiene su función)
- Conexión a base de datos con `pyodbc`
- Validación de contraseñas
- Menús interactivos por consola

## 🛢️ Base de datos

- SQL Server
- Tabla: `Usuarios`
- Campos: Id, Nombre, Usuario, Contraseña (encriptada), Rol

## 🧪 Scripts SQL

Se incluye un archivo `scripts/init_db.sql` con las sentencias necesarias para crear la tabla y realizar operaciones CRUD directamente desde SQL Server Management Studio.

## 🧰 Requisitos para ejecutar

- Python 3.10+
- SQL Server (con ODBC Driver 17)
- Librería `pyodbc` instalada (`pip install pyodbc`)