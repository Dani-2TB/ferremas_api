# Ferremás API

Este en este repositorio se encuentra la API para la app web ferremás la utiliza Django Rest Framework

## ¿Cómo servirse de la API?

La API tiene varios servicios los cuales pueden ser accedidos por el url

**API_ROOT:** <http://host:8000/api>

***

Los endpoints de la api están separados en:

### Auth: Servicio de autenticación

URL_BASE: API_ROOT/auth

### Endpoints

#### register

URL: API_ROOT/auth/register

Ejemplo:

``` http
POST http://127.0.0.1:8000/api/auth/register
Content-Type: application/json

{"username": "testing2", "password":"testing321","email":"example@email.com"}
```

#### login

URL: API_ROOT/auth/login

Método: POST

Ejemplo:

``` http
POST http://127.0.0.1:8000/api/auth/login
Content-Type: application/json

{"username": "admin", "password":"Testing321"}
```

#### test_token

URL: API_ROOT/auth/testToken

Método: GET

Ejemplo:

``` http
GET http://127.0.0.1:8000/api/auth/testToken
Content-Type: application/json
Authorization: Token 5b57235cb76953c7209b2c0d47e0722e348109cf
```

***

### Productos: Servicio de productos

### Endpoints productos

#### agregar producto

URL: API_ROOT/producto/productoList

Método: POST

Ejemplo:

``` http
POST http://localhost:8000/api/productos/productoList/
Content-Type: application/json

{"nombre":"Desatornillador", "precio": 2990,"cantidad": 1, "categoria": 4}
```

#### listar productos

URL: API_ROOT/producto/productoList

Método: GET

Ejemplo:

``` http
POST http://localhost:8000/api/productos/productoList/
Content-Type: application/json
```

#### detalle de producto

URL: API_ROOT/producto/productoDetalle/{pk_producto}

Método: GET

Ejemplo:

``` http
POST http://localhost:8000/api/productos/productoList/
Content-Type: application/json
```
