from django.urls import path
from . import views
urlpatterns = [
    path('', views.generate_wifi_qrcode, name='generate_wifi_qrcode'),
]
