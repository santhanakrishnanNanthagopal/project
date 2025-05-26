from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.create),
    path('user/all_details/', views.get_all_details, name='get_all_details'),
    path('user/<str:name>/', views.user_details, name='user_details')
    
]
