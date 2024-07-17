from django.urls import path
from .views import CrearCarrito, CarritoDetalle

urlpatterns = [
    path("crearCarrito", CrearCarrito.as_view()),
]
