CREATE DATABASE Usuarios_DB;
USE Usuarios_DB;

CREATE TABLE IF NOT EXISTS tipo_usuarios (
id_tipo_usuario INT AUTO_INCREMENT PRIMARY KEY,
nombre_tipo VARCHAR(50) NOT NULL,
descripcion VARCHAR(100) NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
created_by VARCHAR(50),
updated_by VARCHAR(50),
deleted TINYINT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS usuarios (
id_usuario INT AUTO_INCREMENT PRIMARY KEY,
usuario VARCHAR(50) NOT NULL UNIQUE,
contrasena VARCHAR(100) NOT NULL,
tipo_usuario INT,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
created_by VARCHAR(50),
updated_by VARCHAR(50),
deleted TINYINT DEFAULT 0,
CONSTRAINT fk_usuarios_tipo FOREIGN KEY (tipo_usuario) REFERENCES tipo_usuarios(id_tipo_usuario) 
);

INSERT INTO tipo_usuarios (nombre_tipo, descripcion, created_by)
VALUES
	("Admin", "Acceso y permisos total del sistema", "system"),
    ("Usuario", "Acceso limitado", "system");
    
INSERT INTO usuarios (usuario, contrasena, tipo_usuario, created_by)
VALUES
	("Arael", "ara173", 1, "system");
