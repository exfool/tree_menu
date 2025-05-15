from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('about/team/', TemplateView.as_view(template_name='team.html'), name='team'),
    path('about/history/', TemplateView.as_view(template_name='history.html'), name='history'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
]
