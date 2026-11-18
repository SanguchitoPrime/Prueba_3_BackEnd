from django.urls import path
from .views import (
    MaquinariaListView,
    MaquinariaDetailView,
    MaquinariaCreateView,
    MaquinariaUpdateView,
    MaquinariaDeleteView,
)

urlpatterns = [
    path('', MaquinariaListView.as_view(), name='maquinaria_list'),
    path('maquinaria/<int:pk>/', MaquinariaDetailView.as_view(), name='maquinaria_detail'),
    path('nuevo/', MaquinariaCreateView.as_view(), name='maquinaria_create'),
    path('maquinaria/<int:pk>/editar/', MaquinariaUpdateView.as_view(), name='maquinaria_update'),
    path('maquinaria/<int:pk>/eliminar/', MaquinariaDeleteView.as_view(), name='maquinaria_delete'),
]