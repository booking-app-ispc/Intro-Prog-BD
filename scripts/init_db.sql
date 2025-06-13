CREATE DATABASE crudUsers;
GO

USE crudUsers;
GO

CREATE TABLE Usuarios (
    Id INT PRIMARY KEY IDENTITY,
    Nombre NVARCHAR(100),
    Usuario NVARCHAR(50) UNIQUE,
    Contrasena NVARCHAR(100),
    Rol NVARCHAR(20)
);
