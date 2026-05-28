CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE usuarios (
user_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
username VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL UNIQUE,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
created_by INT,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
deleted BOOLEAN DEFAULT 0
);

CREATE TABLE autores (
autor_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
contacto VARCHAR(100) NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
created_by INT,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
deleted BOOLEAN DEFAULT 0
);

CREATE TABLE categorias (
categoria_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
nombre_categoria VARCHAR(100) NOT NULL,
descripcion VARCHAR(100) NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
created_by INT,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
deleted BOOLEAN DEFAULT 0
);

CREATE TABLE estados (
estado_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
nombre_estado VARCHAR(100) NOT NULL,
descripcion VARCHAR(100) NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
created_by INT,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
deleted BOOLEAN DEFAULT 0
);

CREATE TABLE libros (
libro_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
libro_isbn VARCHAR(20) NOT NULL UNIQUE,
titulo VARCHAR(100) NOT NULL,
autor_id INT,
categoria_id INT,
estado_id INT,
CONSTRAINT fk_libro_autor FOREIGN KEY (autor_id) REFERENCES autores(autor_id),
CONSTRAINT fk_libro_categoria FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id),
CONSTRAINT fk_libro_estado FOREIGN KEY (estado_id) REFERENCES estados(estado_id),
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
created_by INT,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
deleted BOOLEAN DEFAULT 0
);

CREATE TABLE prestamos (
prestamo_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
user_id INT,
libro_id INT,
fecha_prestamo DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
fecha_devolucion DATETIME,
CONSTRAINT fk_prestamo_usuario FOREIGN KEY (user_id) REFERENCES usuarios(user_id),
CONSTRAINT fk_prestamo_libro FOREIGN KEY (libro_id) REFERENCES libros(libro_id),
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
created_by INT,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
deleted BOOLEAN DEFAULT 0
);



INSERT INTO usuarios (username, email) VALUES
("Arael", "araelanabalon@liceovvh.cl"),
("Juan", "juandonoso@liceovvh.cl"),
("Jonathan", "jonathanalquinta@liceovvh.cl");

INSERT INTO autores (nombre, contacto) VALUES
("Ernest Hemingway", "hemingway.contacto@email.com"),
("Charles Baudelaire", "baudelaire.archivo@email.com"),
("Antonio Santa Ana", "santaana.autor@email.com");

INSERT INTO categorias (nombre_categoria, descripcion) VALUES
("Novela", "Narraciones extensas en prosa"),
("Poesía", "Poemas en prosa y lírica moderna"),
("Juvenil", "Literatura orientada a jóvenes y adultos");

INSERT INTO estados (nombre_estado, descripcion) VALUES
("Disponible", "El libro está en estantería listo para préstamo"),
("Prestado", "El libro se encuentra en manos de un usuario"),
("Dañado", "El libro requiere reparación o revisión antes de ser prestado");

INSERT INTO libros (libro_isbn, titulo, autor_id, categoria_id, estado_id) VALUES
("9788490622827", "Adiós a las armas", 1, 1, 1),
("9788420684512", "El Spleen de París", 2, 2, 1),
("9789504653110", "Los ojos del perro siberiano", 3, 3, 1);



SELECT * FROM usuarios;
SELECT * FROM autores;
SELECT * FROM libros;
SELECT * FROM estados;
SELECT * FROM categorias;



SELECT user_id, username, email, deleted FROM usuarios;
UPDATE usuarios
SET deleted = 1
WHERE user_id = 1;

SELECT autor_id, nombre, contacto, deleted FROM autores;
UPDATE autores
SET deleted = 1
WHERE autor_id = 3;

SELECT libro_id, libro_isbn, titulo, autor_id, categoria_id, estado_id, deleted FROM libros;
UPDATE libros
SET deleted = 1
WHERE libro_id = 2;

SELECT estado_id, nombre_estado, descripcion, deleted FROM estados;
UPDATE estados
SET nombre_estado = "Roto"
WHERE estado_id = 3;

SELECT categoria_id, nombre_categoria, descripcion, deleted FROM categorias;
UPDATE categorias
SET descripcion = "Literatura más vista por jóvenes"
WHERE categoria_id = 3;






