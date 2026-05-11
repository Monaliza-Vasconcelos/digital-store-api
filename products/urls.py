from django.urls import path

from .views import (
    ProductListView,
    ProductDetailView,
    ProductImageListCreateView,
    ProductImageDetailView
)
from .views import RegisterView

urlpatterns = [
    path("products/", ProductListView.as_view()),
    path("products/<int:pk>/", ProductDetailView.as_view()),

    path("images/", ProductImageListCreateView.as_view()),
    path("images/<int:pk>/", ProductImageDetailView.as_view()),
    path("register/", RegisterView.as_view()),
]