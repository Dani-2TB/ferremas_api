from django.urls import path
from .views import tbk_view, tbk_response_view
urlpatterns = [
    path('crearTransaccion/<int:total>', tbk_view ,name='tbk_view'),
    path('response', tbk_response_view, name='tbk_response_view')
]
