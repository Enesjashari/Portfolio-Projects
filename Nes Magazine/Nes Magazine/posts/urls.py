from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('single/<int:pk>', views.single,name='single'),
    path('header-articles/<int:nid>', views.header_single,name='header-single'),
    path('showbiz-articles/<int:pin>', views.showbiz_single,name='showbiz-single'),
    path('sport-articles/<int:nop>', views.sport_single,name='sport-single'),
    path('travel-articles/<int:suk>', views.travel_single,name='travel-single'),
    path('about', views.about_us,name='about-us'),
    path('contact', views.contact,name='contact'),
    path('category', views.category,name='category'),


]