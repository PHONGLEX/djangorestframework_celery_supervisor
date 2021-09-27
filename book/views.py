from django_filters.rest_framework import DjangoFilterBackend, filterset
from rest_framework.pagination import PageNumberPagination

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .serializers import BookSerializer


class BookPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'count'
    max_page_size = 100
    page_query_param = 'p'


class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    pagination_class = BookPagination

    filterset_fields = ("id", "authors", "title")
    search_fields = ("id", "authors", "title")
    ordering_fields = ("id", "authors", "title")

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)