from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Author, Category, Paper, StudentData
from .serializers import AuthorSerializer, CategorySerializer, PaperSerializer, StudentDataSerializer
from rest_framework import status

# API view to retrieve a list of papers (student data)
class PaperList(APIView):
    def get(self, request):
        # Retrieve all StudentData objects from the database
        papers = StudentData.objects.all()
        
        # Serialize the retrieved data
        serializer = StudentDataSerializer(papers, many=True)
        
        # Return the serialized data as an API response
        return Response(serializer.data)

# API view to retrieve details of a specific paper (student data)
class PaperDetail(APIView):
    def get(self, request, pk):
        try:
            # Retrieve a specific paper using its ID (primary key)
            paper = StudentData.objects.get(id=pk)
        except StudentData.DoesNotExist:
            # Return a 404 response if the paper doesn't exist
            return Response({"detail": "Paper not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the paper data for the response
        serializer = StudentDataSerializer(paper)
        
        # Return the serialized data as an API response
        return Response(serializer.data)

# Similarly structured classes for handling authors and their data
class AuthorList(APIView):
    def get(self, request):
        # Retrieve all Author objects from the database
        authors = Author.objects.all()
        
        # Serialize the retrieved data
        serializer = AuthorSerializer(authors, many=True)
        
        # Return the serialized data as an API response
        return Response(serializer.data)

class AuthorDetail(APIView):
    def get(self, request, pk):
        # Retrieve a specific author using their ID (primary key)
        author = Author.objects.get(pk=pk)
        
        # Serialize the author data for the response
        serializer = AuthorSerializer(author)
        
        # Return the serialized data as an API response
        return Response(serializer.data)

# Similarly structured classes for handling categories and their data
class CategoryList(APIView):
    def get(self, request):
        # Retrieve all Category objects from the database
        categories = Category.objects.all()
        
        # Serialize the retrieved data
        serializer = CategorySerializer(categories, many=True)
        
        # Return the serialized data as an API response
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get(self, request, pk):
        # Retrieve a specific category using its ID (primary key)
        category = Category.objects.get(pk=pk)
        
        # Serialize the category data for the response
        serializer = CategorySerializer(category)
        
        # Return the serialized data as an API response
        return Response(serializer.data)
