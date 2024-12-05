from django.contrib import admin
from . models import Categoria, Pedido, Producto, Inventario, DetallePedido, ImagenProducto

admin.site.register(Categoria)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(DetallePedido)
admin.site.register(ImagenProducto)

