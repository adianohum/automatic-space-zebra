from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import FinanciamentoImovelSeralizer
from financiamentoImovel.models import FinanciamentoImovel


class FinanciamentoImovelListCreate(generics.ListCreateAPIView):
    queryset = FinanciamentoImovel.objects.all()
    serializer_class = FinanciamentoImovelSeralizer