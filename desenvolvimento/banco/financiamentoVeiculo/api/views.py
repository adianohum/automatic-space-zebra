from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import FinanciamentoVeiculoSeralizer
from financiamentoVeiculo.models import FinanciamentoVeiculo


class FinanciamentoVeiculoListCreate(generics.ListCreateAPIView):
    queryset = FinanciamentoVeiculo.objects.all()
    serializer_class = FinanciamentoVeiculoSeralizer