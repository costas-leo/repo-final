class Crud:

    @staticmethod
    def crear_categoria(conexion, nombre, descripcion):
        cursor = conexion.cursor()
        query = "INSERT INTO categorias (nombre, descripcion) VALUES (%s, %s)"
        cursor.execute(query, (nombre, descripcion))
        conexion.commit()
        cursor.close()
        print("Categoría creada exitosamente.")

    @staticmethod
    def crear_producto(conexion, nombre, descripcion, precio, stock, categoria_id):
        cursor = conexion.cursor()
        query = """INSERT INTO productos (nombre, descripcion, precio, stock, categoria_id)
                   VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (nombre, descripcion, precio, stock, categoria_id))
        conexion.commit()
        cursor.close()
        print("Producto creado exitosamente.")

    @staticmethod
    def crear_importador(conexion, nombre, direccion, telefono, email):
        cursor = conexion.cursor()
        query = """INSERT INTO importadores (nombre, direccion, telefono, email)
                   VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (nombre, direccion, telefono, email))
        conexion.commit()
        cursor.close()
        print("Importador creado exitosamente.")

    @staticmethod
    def relacionar_producto_importador(conexion, producto_id, importador_id):
        cursor = conexion.cursor()
        query = """INSERT INTO producto_importador (producto_id, importador_id)
                   VALUES (%s, %s)"""
        cursor.execute(query, (producto_id, importador_id))
        conexion.commit()
        cursor.close()
        print("Producto e importador relacionados exitosamente.")

    @staticmethod
    def registrar_movimiento(conexion, producto_id, tipo, cantidad, observaciones):
        cursor = conexion.cursor()
        query = """INSERT INTO movimientos (producto_id, tipo, cantidad, observaciones)
                   VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (producto_id, tipo, cantidad, observaciones))
        conexion.commit()
        cursor.close()
        print("Movimiento registrado exitosamente.")

    @staticmethod
    def leer_producto(conexion, producto_id):
        cursor = conexion.cursor()
        query = "SELECT * FROM productos WHERE id = %s"
        cursor.execute(query, (producto_id,))
        producto = cursor.fetchone()
        cursor.close()
        print("Producto leído:", producto)

    @staticmethod
    def actualizar_producto(conexion, producto_id, nombre, descripcion, precio, stock, categoria_id):
        cursor = conexion.cursor()
        query = """UPDATE productos
                   SET nombre = %s, descripcion = %s, precio = %s, stock = %s, categoria_id = %s
                   WHERE id = %s"""
        cursor.execute(query, (nombre, descripcion, precio, stock, categoria_id, producto_id))
        conexion.commit()
        cursor.close()
        print("Producto actualizado exitosamente.")

    @staticmethod
    def eliminar_producto(conexion, producto_id):
        cursor = conexion.cursor()
        query = "DELETE FROM productos WHERE id = %s"
        cursor.execute(query, (producto_id,))
        conexion.commit()
        cursor.close()
        print("Producto eliminado exitosamente.")
