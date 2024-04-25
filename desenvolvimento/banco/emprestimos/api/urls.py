from django.urls import path
from .views import SimulacaoEmprestimoCreateView, SimulacaoEmprestimoListView, SimulacaoEmprestimoDetailView, SimularEmprestimoGetView 
 

urlpatterns = [
    path('criar_emprestimos', SimulacaoEmprestimoCreateView.as_view()),
    path('listar_emprestimos/', SimulacaoEmprestimoListView.as_view()),
    path('listar_um_emprestimo/<int:pk>/', SimulacaoEmprestimoDetailView.as_view()),
    path('resultado_simulacao_emprestimo/<str:id>', SimularEmprestimoGetView.as_view())
]