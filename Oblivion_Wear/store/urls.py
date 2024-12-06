from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('generalproducts/', views.generalproducts_view, name='generalproducts'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('paymentsuccesful/', views.paymentsuccesful_view, name='paymentsuccesful'),
    path('product/<int:pk>/', views.product, name='product'),
    path('profile/', views.profile_view, name='profile'),
    path('shippinginfo/', views.shippinginfo_view, name='shippinginfo'),
]




