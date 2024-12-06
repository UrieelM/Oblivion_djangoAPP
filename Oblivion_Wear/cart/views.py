# views.py
from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Producto
from django.http import JsonResponse

# views.py
def cart_summary(request):
    cart = Cart(request)
    # Obtener todos los productos del carrito
    cart_items = cart.cart  # Esto asumirá que 'cart' ya contiene los productos como un diccionario
    return render(request, "cart_summary.html", {'cart_items': cart_items})

# views.py
def cart_add(request):
    cart = Cart(request)
    if request.method == 'POST' and request.POST.get('action') == 'post':
        try:
            product_id = int(request.POST.get('product_id'))
            product = get_object_or_404(Producto, id_producto=product_id)
            cart.add(product=product)

            # Asegúrate de incluir 'sku' al agregar el producto al carrito
            cart.cart[product.id_producto] = {
                'name': product.nombre,
                'price': str(product.precio),
                'image': product.imagen.url if product.imagen else None,
                'size': product.talla,
                'color': product.color,
                'sku': product.sku,  # Aquí aseguramos que 'sku' esté presente
                'quantity': 1,  # O la cantidad que desees
            }

            return JsonResponse({
                'message': 'Product added to cart',
                'product': product.nombre,
                'price': product.precio,
                'cart_total_items': len(cart.cart)
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

def cart_delete(request):
    pass

def cart_update(request):
    pass