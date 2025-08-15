from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate(self, data):
        # validates that age is not in the future
        if data > date.year:
            raise serializers.ValidationError("Age can't be in the future")
        return data
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

(many=True, read_only=True)"