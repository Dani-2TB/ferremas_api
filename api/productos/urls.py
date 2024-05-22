from django.urls import path
from .views import (ProductosRoot, CategoriaList)

urlpatterns = [
    path('', ProductosRoot.as_view(), name='productos-root'),
    path('categoriaList', CategoriaList.as_view(), name='categoriaList')
]