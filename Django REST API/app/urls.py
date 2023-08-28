from django.urls import path
from .views import PaperList, PaperDetail, AuthorList, AuthorDetail, CategoryList, CategoryDetail

# Define URL patterns for API endpoints
urlpatterns = [
    # Endpoint for retrieving the list of papers (student data)
    path('papers/', PaperList.as_view(), name='paper-list'),

    # Endpoint for retrieving details of a specific paper using its ID
    path('papers/<str:pk>/', PaperDetail.as_view(), name='paper-detail'),

    # Endpoint for retrieving the list of authors
    path('authors/', AuthorList.as_view(), name='author-list'),

    # Endpoint for retrieving details of a specific author using their ID
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),

    # Endpoint for retrieving the list of categories
    path('categories/', CategoryList.as_view(), name='category-list'),

    # Endpoint for retrieving details of a specific category using its ID
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
]
