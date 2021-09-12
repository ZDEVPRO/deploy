from django.urls import path
from tarjimon import views

urlpatterns = [
    path('', views.index, name='index'),
]
