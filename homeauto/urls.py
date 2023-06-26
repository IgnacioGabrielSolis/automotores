from django.urls import path
from homeauto import views

urlpatterns = [
    path('', views.index, name='index'),
]