from django.shortcuts import render, redirect, redirect, get_object_or_404
from .models import Producto
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


def home(request):
    productos = Producto.objects.all()

    # Filtra los productos por categorías y ordena antes de hacer el corte
    categoria_1 = Producto.objects.filter(categoria__pk=1).order_by('id_producto')[:3]
    categoria_2 = Producto.objects.filter(categoria__pk=2).order_by('id_producto')[:3]
    
    # Extrae el nombre de la categoría
    nombre_categoria_1 = categoria_1.first().categoria.nombre if categoria_1.exists() else "Categoría no encontrada"
    nombre_categoria_2 = categoria_2.first().categoria.nombre if categoria_2.exists() else "Categoría no encontrada"
    
    return render(request, 'home.html', {
        'productos': productos,
        'categoria_1': categoria_1,
        'categoria_2': categoria_2,
        'nombre_categoria_1': nombre_categoria_1,
        'nombre_categoria_2': nombre_categoria_2
    })



def cart_view(request):
    return render(request, 'cart.html', {})



def checkout_view(request):
    return render(request, 'checkout.html', {})

def generalproducts_view(request):
    categorias = Producto.objects.values_list('categoria', flat=True).distinct()
    
    categoria_seleccionada = request.GET.getlist('category')
    
    if categoria_seleccionada:
        productos = Producto.objects.filter(categoria__in=categoria_seleccionada)
    else:
        productos = Producto.objects.all()
    
    total_productos = productos.count()
    
    return render(request, 'generalproducts.html', {
        'productos': productos,
        'categorias': categorias,
        'categoria_seleccionada': categoria_seleccionada,
        'total_productos': total_productos
    })


def login_user(request):
    if request.method == "POST":
        if 'login' in request.POST:  # Iniciar sesión
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been logged in!")
                return redirect('home')
            else:
                messages.error(request, "Invalid credentials!")
                return redirect('login')
        
        elif 'signup' in request.POST:  # Registrar usuario
            username = request.POST['username']
            password = request.POST['password']
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                login(request, user)
                messages.success(request, "Account created and logged in!")
                return redirect('home')
            except:
                messages.error(request, "Error creating account!")
                return redirect('login')
    
    return render(request, 'loginsignup.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been log out babe see ya! <3"))
    return redirect('home')

def paymentsuccesful_view(request):
    return render(request, 'paymentsuccesful.html', {})


def product(request, pk):
    try:
        producto = Producto.objects.get(id_producto=pk)
        # Obtener los 3 productos más vendidos o cualquier criterio que desees
        productos = Producto.objects.all().order_by('-precio')[:3]  # Cambia el filtro según lo necesites
    except Producto.DoesNotExist:
        producto = None
        productos = []

    return render(request, 'product.html', {'producto': producto, 'productos': productos})




def profile_view(request):
    return render(request, 'profile.html', {})

def shippinginfo_view(request):
    return render(request, 'shippinginfo.html', {})
