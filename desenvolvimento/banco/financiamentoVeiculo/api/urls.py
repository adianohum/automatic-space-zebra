from django.urls import path
from .views import FinanciamentoVeiculoListCreate


urlpatterns = [
    path('financiamento_veiculo/', FinanciamentoVeiculoListCreate.as_view())
]