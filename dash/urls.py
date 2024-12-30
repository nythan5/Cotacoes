from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('historical/<str:moeda>/', views.get_historical_data, name='historical_data'),
]
