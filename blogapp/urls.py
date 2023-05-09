from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('mbtitest/', views.mbtitest, name='mbtitest'),
    path('mbtiresult/', views.mbtiresult, name='mbtiresult'),


   
]