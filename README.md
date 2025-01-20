# Proyecto de Inventario

## Tabla de contenidos
- [Introducción](#introducción)
- [Instalación](#instalación)
- [Cómo usarlo](#cómo-usarlo)
- [Rutas de la API](#rutas-de-la-api)

---

## Introducción
Este proyecto es una aplicación backend diseñada para la gestión de un inventario de productos. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre las categorías y productos, gestionar movimientos de inventario y vincular productos con importadores.

El programa expone una API REST utilizando **Flask** para manejar las operaciones y es compatible con herramientas como **Postman** para realizar pruebas y simulaciones de solicitudes.

---

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd inventario-backend
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install flask
   pip install mysql-connector-python
   ```

---

## Cómo usarlo

Para iniciar la aplicación, ejecuta el siguiente comando:
```bash
python app.py
```

La API estará disponible en `http://127.0.0.1:5000`.

### Ejemplo de uso con Postman
- **Crear un producto:**
  - Ruta: `POST /producto`
  - Body (JSON):
    ```json
    {
        "nombre": "Producto A",
        "descripcion": "Descripcion del producto",
        "precio": 100.5,
        "stock": 50,
        "categoria_id": 1
    }
    ```

- **Leer un producto por ID:**
  - Ruta: `GET /producto/<id>`

- **Actualizar un producto:**
  - Ruta: `PUT /producto/<id>`
  - Body (JSON):
    ```json
    {
        "nombre": "Producto B",
        "descripcion": "Nueva descripcion",
        "precio": 150.0,
        "stock": 30,
        "categoria_id": 2
    }
    ```

- **Eliminar un producto:**
  - Ruta: `DELETE /producto/<id>`

---

## Rutas de la API

### Categorías
- **Crear categoría**
  - Ruta: `POST /categoria`
  - Body (JSON):
    ```json
    {
        "nombre": "Categoria X",
        "descripcion": "Descripcion de la categoria"
    }
    ```

### Productos
- **Crear producto**: `POST /producto`
- **Leer producto por ID**: `GET /producto/<id>`
- **Actualizar producto**: `PUT /producto/<id>`
- **Eliminar producto**: `DELETE /producto/<id>`

### Movimientos
- **Registrar movimiento**
  - Ruta: `POST /movimiento`
  - Body (JSON):
    ```json
    {
        "producto_id": 1,
        "tipo": "entrada",
        "cantidad": 20,
        "observaciones": "Ingreso al inventario"
    }
    ```

### Relaciones
- **Relacionar producto con importador**
  - Ruta: `POST /relacion`
  - Body (JSON):
    ```json
    {
        "producto_id": 1,
        "importador_id": 2
    }
    ```

---

