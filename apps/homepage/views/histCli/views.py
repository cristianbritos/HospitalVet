from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from apps.homepage.models import HistMedEnc, HistMedDet, Mascota, Veterinario

class HistMedEncListView(ListView):
    model = HistMedEnc
    template_name = 'histCli/list.html'
    context_object_name = 'object_list'
    
    def get_queryset(self):
        return HistMedEnc.objects.select_related('mascota', 'veterinario').prefetch_related('histmeddet_set')

class HistMedEncCreateView(CreateView):
    model = HistMedEnc
    fields = ['mascota', 'veterinario', 'fecha_cre', 'alergias', 'detalle']
    template_name = 'histCli/create2.html'
    success_url = reverse_lazy('historial_list')

class HistMedDetCreateView(CreateView):
    model = HistMedDet
    fields = ['fecha', 'motivo_consulta', 'diagnostico', 'tratamiento', 'practicas']
    template_name = 'histCli/create_det.html'

    def form_valid(self, form):
        # Obtener el historial médico (HistMedEnc) al que se asociará este detalle
        historial_medico = get_object_or_404(HistMedEnc, pk=self.kwargs['enc_id'])
        form.instance.HMEnc = historial_medico  # Asignar el historial médico al detalle
        return super().form_valid(form)

    def get_success_url(self):
        # Redirigir a la vista de lista de historiales médicos después de guardar
        return reverse_lazy('historial_list')
