from django.views.generic import TemplateView


class Blog(TemplateView):
    template_name = 'se_dmc/blog.html'