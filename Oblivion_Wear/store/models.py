from django.db import models
from django.core.exceptions import ValidationError


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    
TALLAS_CHOICES = [
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
    ('XXL', 'Double Extra Large'),
    # Add more sizes as needed
]


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    talla = models.CharField(max_length=3, choices=TALLAS_CHOICES, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    imagen = models.ImageField(upload_to="uploads/producto/", blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")
    
    def __str__(self):
        return f"{self.nombre} ({self.sku})"


class ImagenProducto(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, related_name="imagenes", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="uploads/producto/", blank=True, null=True)
    
    def __str__(self):
        return f"Imagen de {self.producto.nombre}"



class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, related_name="inventario")
    cantidad = models.PositiveIntegerField(default=0)  # Solo este campo maneja el inventario

    def __str__(self):
        return f"Inventario de {self.producto.nombre}: {self.cantidad} unidades"


class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('procesado', 'Procesado'),
        ('enviado', 'Enviado'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]
    id_pedido = models.AutoField(primary_key=True)
    usuario_id = models.IntegerField()
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado_pedido = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='pendiente')

    def calcular_total(self):
        self.total = sum(detalle.subtotal for detalle in self.detalles.all())
        self.save()

    def __str__(self):
        return f"Pedido #{self.id_pedido} - {self.get_estado_pedido_display()}"



class DetallePedido(models.Model):
    id_detalle_pedido = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="detalles")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="detalles")
    cantidad = models.PositiveIntegerField()

    @property
    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"Pedido #{self.pedido.id_pedido} - {self.producto.nombre} x {self.cantidad}"

