from django.views.generic import DetailView, TemplateView
from ..models.services import Service
from django.shortcuts import render

class Services(TemplateView):
    template_name = 'se_dmc/services.html'

    def get_context_data(self, **kwargs):
        context = super(Services, self).get_context_data(**kwargs)
        context['service'] = Service.objects.all()
        return context







