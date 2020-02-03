from django.views.generic import TemplateView
from ..models.team import Team


class About(TemplateView):
    template_name = 'se_dmc/about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['team'] = Team.objects.all()[:5]
        return context
