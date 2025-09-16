from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projetos/', views.projects, name='projects'),
    path('projeto/<int:project_id>/', views.project_detail, name='project_detail'),
    path('sobre/', views.about, name='about'),
    path('contato/', views.contact, name='contact'),
]
