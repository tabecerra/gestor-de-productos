from models import Producto

class ProductoController:
    @staticmethod
    def buscar_productos(query):
        return Producto.select(Producto.producto_id, Producto.nombre, Producto.marca, Producto.talle, Producto.cantidad, Producto.precio).where(
        (Producto.nombre ** f'%{query}%') |
        (Producto.marca ** f'%{query}%') |
        (Producto.talle ** f'%{query}%')
    )

    def agregar_producto(nombre, marca, precio, talle, cantidad):
        Producto.create(nombre=nombre, marca=marca, precio=precio, talle=talle, cantidad=cantidad)

    @staticmethod
    def eliminar_producto(producto_id):
        Producto.get_by_id(producto_id).delete_instance()

    @staticmethod
    def descontar_producto(producto_id, cantidad):
        producto = Producto.get_by_id(producto_id)
        producto.precio -= cantidad
        producto.save()

    @staticmethod
    def editar_producto(producto_id, nombre, marca, precio, talle, cantidad):
        producto = Producto.get_by_id(producto_id)
        producto.nombre = nombre
        producto.marca = marca
        producto.precio = precio
        producto.talle = talle
        producto.cantidad = cantidad
        producto.save()

    @staticmethod
    def obtener_producto_por_id(producto_id):
        return Producto.get_by_id(producto_id)  
    
    @staticmethod
    def producto_existente(nombre, marca, talle):
        return Producto.select().where(
            (Producto.nombre == nombre) &
            (Producto.marca == marca) &
            (Producto.talle == talle)
        ).exists()