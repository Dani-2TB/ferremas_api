from django.http import HttpResponse
from django.shortcuts import redirect
from transbank.webpay.webpay_plus.transaction import Transaction

api_key = '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C'
commerce_code = '597055555532'


def tbk_view(request, total):
    transaction = Transaction()
    response = transaction.create(
        buy_order='order12345',
        session_id='session12345',
        amount=total,
        return_url='http://127.0.0.1:8000/api/tbk/response'
    )
    return redirect(response['url'] + '?token_ws=' + response['token'])


def tbk_response_view(request):
    token = request.GET.get('token_ws')
    transaction = Transaction()
    response = transaction.commit(token=token)

    if response['status'] == 'AUTHORIZED':
        return HttpResponse("Transacción Exitosa: " + str(response))
    else:
        return HttpResponse("Transacción Fallida: " + str(response))
