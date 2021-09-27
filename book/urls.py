from django.urls import path

from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path('', BookListCreateView.as_view(), name='list'),
    path('detail/<int:id>/', BookDetailView.as_view(), name='detail')
]