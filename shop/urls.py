from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('', views.index, name='list'),
#   path('shop/', views.index, name='list'),
    path('<int:shop_id>/', views.detail, name='detail'),    
]

