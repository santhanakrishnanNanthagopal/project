from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import create
from . import views
urlpatterns = [
    path('create/',views.create,name='create')
]
