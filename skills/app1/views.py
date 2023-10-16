#from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from app1.models import Ingrediente
from app1.models import Orden
from app1.models import OrdenPlatillo
from app1.models import Categoria
from app1.models import Platillo
from app1.models import PlatilloIngrediente

# Create your views here.
class RetrieveIngrediente(APIView):
        permission_classes = (AllowAny,)

        def get(self, request):
                ingrediente_list = Ingrediente.objects.all().values()
                return Response(ingrediente_list, status=status.HTTP_200_OK)
        