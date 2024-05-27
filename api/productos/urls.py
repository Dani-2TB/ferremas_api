from django.urls import path
from .views import (ProductosRoot, 
                    CategoriaList, CategoriaDetalle,
                    ProductoList, ProductoDetalle)

urlpatterns = [
    path('', ProductosRoot.as_view(), name='productos-root'),
    path('categoriaList', CategoriaList.as_view(), name='categoriaList'),
    path('categoriaDetalle/<int:pk>', CategoriaDetalle.as_view()),
    path('productoList/', ProductoList.as_view()),
    path('productoDetalle/<int:pk>', ProductoDetalle.as_view())
]