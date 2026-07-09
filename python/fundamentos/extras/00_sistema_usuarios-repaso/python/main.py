import os
from usuarios import Usuario

def cls_consola():
    os.system("cls")


usuario_logeado = None
tipo_sesion = None

while True:
    print("\n--- SISTEMA DE USUARIOS ---")
    if usuario_logeado:
        rol_texto = "Administrador" if tipo_sesion == 1 else "Usuario Estándar"
        print(f"Sesión activa: {usuario_logeado} | Rol: {rol_texto}")
    else:
        print("Estado: No has iniciado sesión. (Usa la opción 6 para ingresar)")
    print("-" * 27)
    print("1. Registrar usuario (Solo Admin)")
    print("2. Buscar usuario (Solo Admin)")
    print("3. Listar usuarios (Solo Admin)")
    print("4. Modificar usuario (Solo Admin)")
    print("5. Eliminar usuario (Solo Admin)")
    print("6. Iniciar Sesión / Cerrar Sesión")
    print("0. Salir del programa")
    opcion = input("\nIngrese una opción: ")

    if opcion in ["1", "2", "3", "4", "5"]:
        if not usuario_logeado:
            cls_consola()
            print("Acceso denegado: Debes iniciar sesión primero (Opción 6).")
            continue
        if tipo_sesion != 1:
            cls_consola()
            print("Acceso denegado: Tu cuenta no tiene permisos de Administrador.")
            continue

    if opcion == "1":
        cls_consola()
        username = input("Ingrese un nombre de usuario: ")
        password = input("Ingrese una contraseña: ")
        print("Tipos disponibles: 1 = Admin, 2 = Usuario")
        tipo = int(input("Ingrese el tipo de usuario (1 o 2): "))
        usuario = Usuario(username, password, tipo_usuario = tipo)
        usuario.crear_usuario()

    elif opcion == "2":
        cls_consola()
        id_buscar = input("Ingrese el ID del usuario a buscar: ")
        resultado = Usuario.buscar_usuario(id_buscar)
        if resultado:
            id_u, name_u, tipo_u = resultado
            print(f"\nID: {id_u}")
            print(f"Usuario: {name_u}")
            print(f"Tipo: {tipo_u} ({'Admin' if tipo_u == 1 else 'Usuario'})")
        else:
            print("Usuario no encontrado.")

    elif opcion == "3":
        cls_consola()
        usuarios = Usuario.listado_usuarios()
        if usuarios:
            print("\n--- LISTADO DE USUARIOS ---")
            for u in usuarios:
                id_u, name_u, tipo_u = u
                rol = "Admin" if tipo_u == 1 else "Usuario"
                print(f"ID: {id_u} | Usuario: {name_u} | Rol: {rol}")
        else:
            print("No hay usuarios registrados.")

    elif opcion == "4":
        cls_consola()
        id_usuario = input("Ingrese el ID del usuario a modificar: ")
        print("Nuevos tipos: 1 = Admin, 2 = Usuario")
        nuevo_tipo = int(input("Ingrese el nuevo tipo de usuario: "))
        Usuario.modificar_usuario(nuevo_tipo, id_usuario)
        print("Usuario modificado correctamente.")

    elif opcion == "5":
        cls_consola()
        id_usuario = input("Ingrese el ID del usuario a eliminar: ")
        Usuario.eliminar_usuario(id_usuario)

    elif opcion == "6":
        cls_consola()
        if usuario_logeado:
            Usuario.cerrar_sesion(usuario_logeado)
            usuario_logeado = None
            tipo_sesion = None
        else:
            print("--- INICIAR SESIÓN ---")
            user = input("Usuario: ")
            password = input("Contraseña: ")
            resultado = Usuario.validar_acceso(user, password)
            if resultado:
                id_u, name_u, tipo_u = resultado
                usuario_logeado = name_u
                tipo_sesion = int(tipo_u)
                cls_consola()
                print(f"¡Bienvenido de nuevo, {usuario_logeado}!")
            else:
                print("Usuario o contraseña incorrectos.")

    elif opcion == "0":
        cls_consola()
        print("Saliendo del programa...")
        break

    else:
        cls_consola()
        print("Opción inválida.")
