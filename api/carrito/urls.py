from django.urls import path
from .views import CarritoAPI

urlpatterns = [
    path("carritoView", CarritoAPI.as_view(), name='carrito')
]
