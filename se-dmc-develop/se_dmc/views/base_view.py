from django.views.generic import DetailView

from ..models import Address


class BaseView(DetailView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        address = Address.objects.all()[0]
        context.update(address=address)
        return context
    