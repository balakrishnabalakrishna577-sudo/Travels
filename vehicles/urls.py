from django.urls import path
from . import views

urlpatterns = [
    path('airport-transfer/', views.airport_transfer, name='airport_transfer'),
    path('airport-transfer/success/<str:booking_id>/', views.airport_transfer_success, name='airport_transfer_success'),
]
