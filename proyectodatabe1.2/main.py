from conexion import Cconexion
from crud import Crud

def main():
    conexion = Cconexion.conexionDataBase()

    if conexion:
        print("\nConexión establecida con la base de datos.")

        while True:
            print("\nMenú principal:")
            print("1. Ingresar nueva categoría")
            print("2. Ingresar nuevo producto")
            print("3. Ingresar nuevo importador")
            print("4. Actualizar producto")
            print("5. Mostrar un producto")
            print("6. Eliminar un producto")
            print("7. Registrar movimiento de inventario")
            print("8. Relacionar producto e importador (automático)")
            print("9. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                # Ingresar nueva categoría
                nombre = input("Ingrese el nombre de la categoría: ")
                descripcion = input("Ingrese la descripción de la categoría: ")
                Crud.crear_categoria(conexion, nombre, descripcion)

            elif opcion == "2":
                # Ingresar nuevo producto
                nombre = input("Ingrese el nombre del producto: ")
                descripcion = input("Ingrese la descripción del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                stock = int(input("Ingrese el stock inicial del producto: "))
                categoria_id = int(input("Ingrese el ID de la categoría asociada: "))
                Crud.crear_producto(conexion, nombre, descripcion, precio, stock, categoria_id)

            elif opcion == "3":
                # Ingresar nuevo importador
                nombre = input("Ingrese el nombre del importador: ")
                direccion = input("Ingrese la dirección del importador: ")
                telefono = input("Ingrese el teléfono del importador: ")
                email = input("Ingrese el email del importador: ")
                Crud.crear_importador(conexion, nombre, direccion, telefono, email)

            elif opcion == "4":
                # Actualizar producto
                producto_id = int(input("Ingrese el ID del producto a actualizar: "))
                nombre = input("Ingrese el nuevo nombre del producto: ")
                descripcion = input("Ingrese la nueva descripción del producto: ")
                precio = float(input("Ingrese el nuevo precio del producto: "))
                stock = int(input("Ingrese el nuevo stock del producto: "))
                categoria_id = int(input("Ingrese el nuevo ID de la categoría asociada: "))
                Crud.actualizar_producto(conexion, producto_id, nombre, descripcion, precio, stock, categoria_id)

            elif opcion == "5":
                # Mostrar un producto
                producto_id = int(input("Ingrese el ID del producto a mostrar: "))
                Crud.leer_producto(conexion, producto_id)

            elif opcion == "6":
                # Eliminar un producto
                producto_id = int(input("Ingrese el ID del producto a eliminar: "))
                Crud.eliminar_producto(conexion, producto_id)

            elif opcion == "7":
                # Registrar movimiento de inventario
                producto_id = int(input("Ingrese el ID del producto: "))
                tipo = input("Ingrese el tipo de movimiento (entrada/salida): ")
                cantidad = int(input("Ingrese la cantidad: "))
                observaciones = input("Ingrese las observaciones del movimiento: ")
                Crud.registrar_movimiento(conexion, producto_id, tipo, cantidad, observaciones)

            elif opcion == "8":
                # Relacionar producto e importador (automático)
                print("\nRelación automática entre producto e importador:")
                producto_id = 1  # Cambia este valor por el ID del producto deseado
                importador_id = 1  # Cambia este valor por el ID del importador deseado
                Crud.relacionar_producto_importador(conexion, producto_id, importador_id)

            elif opcion == "9":
                # Salir del programa
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

        # Cerrar la conexión después de salir del programa
        conexion.close()

    else:
        print("No se pudo conectar a la base de datos.")

if __name__ == "__main__":
    main()
