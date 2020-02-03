"""se_dmc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import Blog, HomeView, Services, Work, WorkSingle, About, Contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home_url'),
    path('blog', Blog.as_view(), name='blog'),
    path('about', About.as_view(), name='about'),
    # path('contact', Contact.as_view(), name='contact'),
    path('services', Services.as_view(), name='services'),
    path('work', Work.as_view(), name='work'),
    path('work-single', WorkSingle.as_view(), name='work-single'),
    path('contact', Contact.index, name='contact'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)