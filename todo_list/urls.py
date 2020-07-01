from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('cross_off/<list_id>/', views.cross_off, name='cross_off'),
    path('uncross/<list_id>/', views.uncross, name='uncross'),
    path('delete/<list_id>/', views.delete, name='delete'),
    path('edit/<list_id>/', views.edit, name='edit'),
]