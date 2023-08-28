from rest_framework import serializers
from .models import Author, Category, StudentData

# Serializer for Author model
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'  # Serialize all fields in the Author model

# Serializer for Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Serialize all fields in the Category model

# Serializer for Paper (StudentData) model
class PaperSerializer(serializers.ModelSerializer):
    # Serialize authors and categories as nested JSON objects using their respective serializers
    authors = AuthorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = StudentData
        fields = '__all__'  # Serialize all fields in the StudentData model

# Custom serializer for StudentData model
class StudentDataSerializer(serializers.ModelSerializer):
    # Serialize authors and categories as JSON fields
    authors = serializers.JSONField()
    categories = serializers.JSONField()

    class Meta:
        model = StudentData
        fields = '__all__'  # Serialize all fields in the StudentData model

    # Convert authors and categories from comma-separated strings to lists
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['authors'] = instance.authors.split(',') if instance.authors else []
        representation['categories'] = instance.categories.split(',') if instance.categories else []
        return representation
