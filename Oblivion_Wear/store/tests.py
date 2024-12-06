from django.test import TestCase
from decimal import Decimal
from django.contrib.auth.models import User
from .models import Categoria, Producto, ImagenProducto, Inventario, Pedido, DetallePedido

class CategoriaTestCase(TestCase):
    def test_create_categoria(self):
        """Test para crear una categoría"""
        categoria = Categoria.objects.create(nombre="Ropa", descripcion="Ropa para todas las edades")
        self.assertEqual(categoria.nombre, "Ropa")
        self.assertEqual(categoria.descripcion, "Ropa para todas las edades")

    def test_update_categoria(self):
        """Test para actualizar una categoría"""
        categoria = Categoria.objects.create(nombre="Electrónicos", descripcion="Pantalones electrónicos")
        categoria.nombre = "Electrónica de consumo"
        categoria.save()
        updated_categoria = Categoria.objects.get(id_categoria=categoria.id_categoria)
        self.assertEqual(updated_categoria.nombre, "Electrónica de consumo")

    def test_delete_categoria(self):
        """Test para eliminar una categoría"""
        categoria = Categoria.objects.create(nombre="Faldas", descripcion="Productos para faldas")
        categoria_id = categoria.id_categoria
        categoria.delete()
        with self.assertRaises(Categoria.DoesNotExist):
            Categoria.objects.get(id_categoria=categoria_id)

class ProductoTestCase(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre="Ropa", descripcion="Ropa casual y formal")

    def test_create_producto(self):
        """Test para crear un producto"""
        producto = Producto.objects.create(
            sku="12345ABC",
            nombre="Camisa casual",
            descripcion="Camisa de algodón, color azul",
            precio=299.99,
            talla="M",
            categoria=self.categoria
        )
        self.assertEqual(producto.sku, "12345ABC")
        self.assertEqual(producto.nombre, "Camisa casual")
        self.assertEqual(producto.precio, 299.99)
        self.assertEqual(producto.talla, "M")

    def test_update_producto(self):
        """Test para actualizar un producto"""
        producto = Producto.objects.create(
            sku="56789DEF",
            nombre="Pantalón formal",
            descripcion="Pantalón de vestir, color negro",
            precio=499.99,
            categoria=self.categoria
        )
        producto.precio = 450.00
        producto.save()
        updated_producto = Producto.objects.get(id_producto=producto.id_producto)
        self.assertEqual(updated_producto.precio, 450.00)

    def test_delete_producto(self):
        """Test para eliminar un producto"""
        producto = Producto.objects.create(
            sku="11122XYZ",
            nombre="Zapatos deportivos",
            descripcion="Zapatos cómodos para correr",
            precio=799.99,
            categoria=self.categoria
        )
        producto_id = producto.id_producto
        producto.delete()
        with self.assertRaises(Producto.DoesNotExist):
            Producto.objects.get(id_producto=producto_id)

class InventarioTestCase(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre="Accesorios", descripcion="Accesorios de moda")
        self.producto = Producto.objects.create(
            sku="A123456",
            nombre="Bolso",
            descripcion="Bolso de cuero",
            precio=999.99,
            categoria=self.categoria
        )

    def test_create_inventario(self):
        """Test para crear inventario"""
        inventario = Inventario.objects.create(producto=self.producto, cantidad=20)
        self.assertEqual(inventario.cantidad, 20)

    def test_update_inventario(self):
        """Test para actualizar inventario"""
        inventario = Inventario.objects.create(producto=self.producto, cantidad=15)
        inventario.cantidad = 10
        inventario.save()
        updated_inventario = Inventario.objects.get(id_inventario=inventario.id_inventario)
        self.assertEqual(updated_inventario.cantidad, 10)

class PedidoTestCase(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre="Deportes", descripcion="Ropa y accesorios deportivos")
        self.producto = Producto.objects.create(
            sku="D123456",
            nombre="Guantes",
            descripcion="Guantes para gimnasio",
            precio=199.99,
            categoria=self.categoria
        )
        self.usuario_id = 1

    def test_create_pedido(self):
        """Test para crear un pedido con un detalle"""
        pedido = Pedido.objects.create(usuario_id=self.usuario_id)
        DetallePedido.objects.create(pedido=pedido, producto=self.producto, cantidad=2)
        pedido.calcular_total()

        self.assertEqual(pedido.total, Decimal('399.98'))

    def test_update_pedido_estado(self):
        """Test para actualizar el estado de un pedido"""
        pedido = Pedido.objects.create(usuario_id=self.usuario_id, estado_pedido="pendiente")
        pedido.estado_pedido = "procesado"
        pedido.save()
        updated_pedido = Pedido.objects.get(id_pedido=pedido.id_pedido)
        self.assertEqual(updated_pedido.estado_pedido, "procesado")

