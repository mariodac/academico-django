from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:matricula_id>', views.edu, name='edu'),
]
