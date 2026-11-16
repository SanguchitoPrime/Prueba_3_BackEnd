from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Maquinaria
from .forms import MaquinariaForm


class MaquinariaListView(ListView):
    model = Maquinaria
    template_name = 'gestion/maquinaria_list.html'
    context_object_name = 'maquinarias'
    queryset = Maquinaria.objects.select_related('tipo').all()


class MaquinariaDetailView(DetailView):
    model = Maquinaria
    template_name = 'gestion/maquinaria_detail.html'
    context_object_name = 'maquinaria'


class MaquinariaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Maquinaria
    form_class = MaquinariaForm
    template_name = 'gestion/maquinaria_form.html'
    success_url = reverse_lazy('maquinaria_list')
    success_message = "La maquinaria '%(nombre)s' fue registrada exitosamente."


class MaquinariaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Maquinaria
    form_class = MaquinariaForm
    template_name = 'gestion/maquinaria_form.html'
    success_url = reverse_lazy('maquinaria_list')
    success_message = "Los datos de '%(nombre)s' fueron actualizados."


class MaquinariaDeleteView(LoginRequiredMixin, DeleteView):
    model = Maquinaria
    template_name = 'gestion/maquinaria_confirm_delete.html'
    success_url = reverse_lazy('maquinaria_list')

    def form_valid(self, form):
        messages.success(self.request, f"El equipo '{self.object.nombre}' fue eliminado del sistema.")
        return super().form_valid(form)