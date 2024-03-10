from django.urls import path, include
from . import views

app_name = 'core'
urlpatterns = [
    path('dashboard/', views.getDashboard, name='dashboard'),
]