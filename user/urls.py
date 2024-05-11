from django.urls import path, include

from . import views


urlpatterns=[
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('read/', views.read, name='read'),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name = 'delete'),
    path('auth/<str:UID>/', views.get_token, name='get_token'),
    path('analytics/<str:UID>/', views.analytics, name='analytics')
    
]