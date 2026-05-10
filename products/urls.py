from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductImageListCreateView
)

urlpatterns = [
    path("products/", ProductListView.as_view()),
    path("products/<int:pk>/", ProductDetailView.as_view()),
    path("images/", ProductImageListCreateView.as_view()),
]