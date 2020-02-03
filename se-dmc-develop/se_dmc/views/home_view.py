from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'se_dmc/index.html'
