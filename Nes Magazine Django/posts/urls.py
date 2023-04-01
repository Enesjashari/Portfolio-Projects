from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('search', views.search,name='search'),
    path('single/<int:pk>', views.single,name='single'),
    path('header-article/<int:nid>', views.header_single,name='header-single'),
    path('showbiz-article/<int:pin>', views.showbiz_single,name='showbiz-single'),
    path('tech-article/<int:pin>', views.tech_single,name='tech-single'),
    path('sport-article/<int:nop>', views.sport_single,name='sport-single'),
    path('travel-article/<int:suk>', views.travel_single,name='travel-single'),
    path('about', views.about_us,name='about-us'),
    path('contact', views.contact,name='contact'),
    path('category', views.category,name='category'),
    #Sport Categories
    path('sport', views.sport_category,name='sport-category'),
    path('sport-2', views.sport_category_2,name='sport-category-2'),
    path('sport-3', views.sport_category_3,name='sport-category-3'),
    path('sport-4', views.sport_category_4,name='sport-category-4'),
    path('sport-5', views.sport_category_5,name='sport-category-5'),
    #end sport
    #Travel categories
    path('travel', views.travel_category,name='travel-category'),
    path('travel-2', views.travel_category_2,name='travel-category-2'),
    path('travel-3', views.travel_category_3,name='travel-category-3'),
    path('travel-4', views.travel_category_4,name='travel-category-4'),
    path('travel-5', views.travel_category_5,name='travel-category-5'),
    #end travel
    #Showbiz Categories
    path('showbiz', views.showbiz_category,name='showbiz-category'),
    path('showbiz-2', views.showbiz_category_2,name='showbiz-category-2'),
    path('showbiz-3', views.showbiz_category_3,name='showbiz-category-3'),
    path('showbiz-4', views.showbiz_category_4,name='showbiz-category-4'),
    path('showbiz-5', views.showbiz_category_5,name='showbiz-category-5'),
    #end showbiz
    #Technology Categories
    path('tech', views.tech_category,name='tech-category'),
    path('tech-2', views.tech_category_2,name='tech-category-2'),
    path('tech-3', views.tech_category_3,name='tech-category-3'),
    path('tech-4', views.tech_category_4,name='tech-category-4'),
    path('tech-5', views.tech_category_5,name='tech-category-5'),    
    #end technology
]