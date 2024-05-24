from django.urls import path
from .views import (ProductosRoot, 
                    CategoriaList, CategoriaDetalle, 
                    SubcategoriaList, SubcategoriaDetalle,
                    ProductoList, ProductoDetalle)

urlpatterns = [
    path('', ProductosRoot.as_view(), name='productos-root'),
    path('categoriaList', CategoriaList.as_view(), name='categoriaList'),
    path('categoriaDetalle/<int:pk>', CategoriaDetalle.as_view()),
    path('subcategoriaList/', SubcategoriaList.as_view()),
    path('subcategoriaDetalle/<int:pk>', SubcategoriaDetalle.as_view()),
    path('productoList/', ProductoList.as_view()),
    path('productoDetalle/<int:pk>', ProductoDetalle.as_view())
]