from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('panel/', views.panel, name='panel'),
    path('logout/', views.logout, name='logout')

]
