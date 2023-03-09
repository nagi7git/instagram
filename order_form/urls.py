
from django.urls import path, include
from . import views

app_name = 'order_form'

urlpatterns = [
    path('', views.order_create, name="order_create"),
    path('status', views.status, name="status"),  
    path('order', views.order, name="order"),
    path('order/<int:pk>/delete', views.order_delete, name="order_delete"),
]