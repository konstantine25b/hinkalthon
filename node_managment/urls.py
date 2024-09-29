from django.urls import path
from . import views


urlpatterns = [
    path('node/', views.NodeListCreateView.as_view(), name='node-list-create'),
    path('data/', views.DataListCreateView.as_view(), name='data-list-create'), 
    path('datacheck/<int:pk>/', views.DataDetailView.as_view(), name='data-detail'),  
]   