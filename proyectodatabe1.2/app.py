from flask import Flask, request, jsonify
from conexion import Cconexion
from crud import Crud

app = Flask(__name__)

# Conexión a la base de datos
conexion = Cconexion.conexionDataBase()

# Rutas para el CRUD
@app.route('/categoria', methods=['POST'])
def crear_categoria():
    data = request.get_json()
    nombre = data.get('nombre')
    descripcion = data.get('descripcion')
    Crud.crear_categoria(conexion, nombre, descripcion)
    return jsonify({"message": "Categoría creada exitosamente."}), 201

@app.route('/producto', methods=['POST'])
def crear_producto():
    data = request.get_json()
    nombre = data.get('nombre')
    descripcion = data.get('descripcion')
    precio = data.get('precio')
    stock = data.get('stock')
    categoria_id = data.get('categoria_id')
    Crud.crear_producto(conexion, nombre, descripcion, precio, stock, categoria_id)
    return jsonify({"message": "Producto creado exitosamente."}), 201

@app.route('/producto/<int:producto_id>', methods=['GET'])
def leer_producto(producto_id):
    producto = Crud.leer_producto(conexion, producto_id)
    if producto:
        return jsonify(producto), 200
    else:
        return jsonify({"message": "Producto no encontrado."}), 404

@app.route('/producto/<int:producto_id>', methods=['PUT'])
def actualizar_producto(producto_id):
    data = request.get_json()
    nombre = data.get('nombre')
    descripcion = data.get('descripcion')
    precio = data.get('precio')
    stock = data.get('stock')
    categoria_id = data.get('categoria_id')
    Crud.actualizar_producto(conexion, producto_id, nombre, descripcion, precio, stock, categoria_id)
    return jsonify({"message": "Producto actualizado exitosamente."}), 200

@app.route('/producto/<int:producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    Crud.eliminar_producto(conexion, producto_id)
    return jsonify({"message": "Producto eliminado exitosamente."}), 200

@app.route('/movimiento', methods=['POST'])
def registrar_movimiento():
    data = request.get_json()
    producto_id = data.get('producto_id')
    tipo = data.get('tipo')
    cantidad = data.get('cantidad')
    observaciones = data.get('observaciones')
    Crud.registrar_movimiento(conexion, producto_id, tipo, cantidad, observaciones)
    return jsonify({"message": "Movimiento registrado exitosamente."}), 201

@app.route('/relacion', methods=['POST'])
def relacionar_producto_importador():
    data = request.get_json()
    producto_id = data.get('producto_id')
    importador_id = data.get('importador_id')
    Crud.relacionar_producto_importador(conexion, producto_id, importador_id)
    return jsonify({"message": "Producto relacionado con importador exitosamente."}), 201

# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
    