from django.views.generic import RedirectView

class RedirectRoot(RedirectView):
    permanent = True
    pattern_name = 'api-root'

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ApiRoot(APIView):
    def get(self, request):
        return Response({"detail":"Esta es la raiz de la API!"})
