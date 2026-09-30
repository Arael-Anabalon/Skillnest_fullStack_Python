import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, password) 
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);
        """
        return connectToMySQL('esquema_usuarios').query_db(query, data)

    @classmethod
    def get_by_email(cls, email):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        data = {'email': email}
        results = connectToMySQL('esquema_usuarios').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        data = {'id': id}
        results = connectToMySQL('esquema_usuarios').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validar_registro(data):
        is_valid = True
        
        # Validar Nombre
        if len(data['nombre'].strip()) < 2 or not data['nombre'].isalpha():
            flash("El nombre debe tener al menos 2 caracteres y contener solo letras.", "registro")
            is_valid = False
            
        # Validar Apellido
        if len(data['apellido'].strip()) < 2 or not data['apellido'].isalpha():
            flash("El apellido debe tener al menos 2 caracteres y contener solo letras.", "registro")
            is_valid = False
            
        # Validar Email (Formato y Existencia)
        if not EMAIL_REGEX.match(data['email']):
            flash("El formato de correo electrónico no es válido.", "registro")
            is_valid = False
        elif Usuario.get_by_email(data['email']):
            flash("El correo electrónico ya se encuentra registrado.", "registro")
            is_valid = False
            
        # Validar Contraseña
        if len(data['password']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "registro")
            is_valid = False
            
        # Confirmar Contraseña
        if data['password'] != data['confirm_password']:
            flash("Las contraseñas no coinciden.", "registro")
            is_valid = False
            
        return is_valid
