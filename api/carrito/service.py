from decimal import Decimal

from django.conf import settings

from api.productos.serializers import ProductoSerializer
from api.productos.models import Producto


class Cart:
    def __init__(self, request):
        """
        Iniciar Carrito
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self, producto, cantidad=1, overide_quantity=False):
        """
        Añadir o modificar la cantidad del item en carrito
        """

        producto_id = str(producto["id"])
        if producto_id not in self.cart:
            self.cart[producto_id] = {
                "cantidad": 0,
                "precio": str(producto["precio"])
            }
        if overide_quantity:
            self.cart[producto_id]["cantidad"] = cantidad 
        else:
            self.cart[producto_id]["cantidad"] += cantidad 
        self.save()

    def remove(self, producto):
        """
        Eliminar producto del carrito
        """
        producto_id = str(producto["id"])

        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()

    def __iter__(self):
        """
        Iterar por items del carrito y buscar los productos de la base de datos
        """
        product_ids = self.cart.keys()
        productos = Producto.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for producto in productos:
            cart[str(producto.id)]["producto"] = ProductoSerializer(producto).data
        for item in cart.values():
            item["precio"] = Decimal(item["precio"]) 
            item["precio_total"] = item["precio"] * item["cantidad"]
            yield item

    def __len__(self):
        """
        Contar items en el carrito
        """
        return sum(item["cantidad"] for item in self.cart.values())

    def get_precio_total(self):
        return sum(Decimal(item["precio"]) * item["cantidad"] for item in self.cart.values())

    def clear(self):
        # eliminar carrito de la sesión
        del self.session[settings.CART_SESSION_ID]
        self.save()