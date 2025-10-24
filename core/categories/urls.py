from django.urls import path
from .views import CategoryCreateView, CategoryListView, CategoryEditView, CategoryDeleteView, CategoryDetailView

urlpatterns = [
    path("", CategoryListView.as_view(), name="category-list"),
    path("create/", CategoryCreateView.as_view(), name="category-create"),
    path("<int:pk>/edit/", CategoryEditView.as_view(), name="category-edit"),
    path("<int:pk>/delete/", CategoryDeleteView.as_view(), name="category-delete"),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]