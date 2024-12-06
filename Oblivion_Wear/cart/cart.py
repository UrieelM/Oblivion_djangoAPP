from store.models import Producto

class Cart():
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('session_key', {})
        if 'session_key' not in self.session:
            self.session['session_key'] = self.cart

    def add(self, product):
        product_id = str(product.id_producto)  # Usar id_producto como clave
        if product_id not in self.cart:
            self.cart[product_id] = {
                'name': product.nombre,
                'price': str(product.precio),
                'quantity': 1,
                'image': product.imagen.url if product.imagen else None,
                'size': product.talla,
                'color': product.color,
            }
        else:
            self.cart[product_id]['quantity'] += 1

        self.session.modified = True


    def get_prods(self):
            product_ids = self.cart.keys()
            products = Producto.objects.filter(id__in=product_ids)

            return products

