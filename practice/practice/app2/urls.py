from django.urls import path
from . import views
urlpatterns= [path('', views.index, name="index"),path("temp1",views.temp1)]