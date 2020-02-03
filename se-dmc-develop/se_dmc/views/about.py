from django.views.generic import TemplateView
# from ..models.team import Team
from ..models import Team, Testimonial


class About(TemplateView):
    template_name = 'se_dmc/about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['team'] = Team.objects.all()[:5]
        return context

class Testimonals(TemplateView):
    template_name = 'se_dmc/about.html'

    def get_context_data(self, **kwargs):
        context = super(Testimonals, self).get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.all()[:5]
        return context
