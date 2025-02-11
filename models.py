from peewee import Model, SqliteDatabase, CharField, DecimalField, IntegerField, AutoField

database = SqliteDatabase('catalogo.db')

class Producto(Model):
    producto_id = AutoField()
    nombre = CharField()
    marca = CharField()
    talle = CharField()
    cantidad = IntegerField()
    precio = DecimalField()

    class Meta:
        database = database
        table_name = 'productos'


database.connect()

database.create_tables([Producto], safe=True)

productos = Producto.select()
if productos.exists():
    for producto in productos:
        print(f"Nombre: {producto.nombre}, Marca: {producto.marca}, Talle: {producto.talle}, Cantidad: {producto.cantidad}, Precio: {producto.precio}, Id: {producto.producto_id}")
else:
    print("No hay productos")

database.close()
