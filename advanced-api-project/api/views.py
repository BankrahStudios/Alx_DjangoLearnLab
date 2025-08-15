from django.shortcuts import render
from .models import Author, Book
from .serializers import BookSerializer, AuthorSerializer
# from django_filters import rest_framework
from rest_framework import generics, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser

# Create your views here.

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    # def get_queryset(self, id):
    #     return Book.objects.filter(id=id)
    
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]


class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]