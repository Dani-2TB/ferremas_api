from django.urls import path
from .views import Register, Login, AutenticarToken

urlpatterns = [
    path('login', Login.as_view(), name='auth-login'),
    path('register', Register.as_view(), name='auth-registrar'),
    path('testToken', AutenticarToken.as_view(), name='auth-testToken')
]