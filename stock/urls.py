from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addItem', views.addItem, name='addItem'),
    path('deleteItem/<id>/', views.deleteItem, name='deleteItem'),
]
