from rest_framework.views import APIView
from rest_framework.response import Response
from .service import Cart
from rest_framework import status

class CarritoAPI(APIView):
    """
    Single API to handle cart operations
    """
    def get(self, request, format=None):
        cart = Cart(request)

        return Response(
            {"data": list(cart.__iter__()), 
            "precio_total": cart.get_precio_total()},
            status=status.HTTP_200_OK
            )

    def post(self, request, **kwargs):
        cart = Cart(request)

        if "remove" in request.data:
            producto = request.data["producto"]
            cart.remove(producto)

        elif "clear" in request.data:
            cart.clear()

        else:
            producto = request.data
            cart.add(
                    producto=producto["producto"],
                    cantidad=producto["cantidad"],
                    overide_quantity=producto["overide_quantity"] if "overide_quantity" in producto else False
                )

        return Response(
            {"message": "cart updated"},
            status=status.HTTP_202_ACCEPTED)

