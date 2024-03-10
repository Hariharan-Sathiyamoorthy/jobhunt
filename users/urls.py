
from django.urls import path, include
from . import views
app_name = 'users'
urlpatterns = [
    path('login/', views.userLogin, name='login'),
    path('register/', views.userRegister, name='register'),
    path('logout/', views.userLogout, name='logout'),
]