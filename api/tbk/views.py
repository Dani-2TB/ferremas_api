from django.http import HttpResponse
from django.shortcuts import redirect, render
from transbank.webpay.webpay_plus.transaction import Transaction
from random import randint
from api.carrito.models import Boleta

api_key = '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C'
commerce_code = '597055555532'


def tbk_view(request, total):
    transaction = Transaction()
    buy_order = "TA" + str(randint(0,99999))
    session_id = "SN" + str(randint(0,99999))
    response = transaction.create(
        buy_order=buy_order,
        session_id=session_id,
        amount=total,
        return_url='http://127.0.0.1:8000/api/tbk/response'
    )
    return redirect(response['url'] + '?token_ws=' + response['token'])


def tbk_response_view(request):
    token = request.GET.get('token_ws')
    transaction = Transaction()
    response = transaction.commit(token=token)

    if response['status'] == 'AUTHORIZED':
        new_boleta = Boleta.objects.create(total=response["amount"])
        new_boleta.save()
        return render(request, 'aceptado.html')
    else:
        return render(request, 'rechazado.html')
