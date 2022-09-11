from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('main',views.main,name='main'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('delete/<int:op>',views.delete,name='delete'),
    path('search',views.search,name='search'),
    path('create',views.create,name='create'),
    path('mark-as-completed/<int:id>', views.mark_as_completed, name="mark-as-completed"),


]