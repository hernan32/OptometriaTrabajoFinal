from django.urls import path

from . import views
from .views import robots_txt

urlpatterns = [
    path('', views.index, name='index'),
    path("robots.txt", robots_txt),
]
