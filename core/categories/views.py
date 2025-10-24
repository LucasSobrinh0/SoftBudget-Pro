from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from rest_framework import generics, permissions

# Views para os produtos

class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # nao precisa avisar sobre pk, pois ele ja tem


class CategoryEditView(generics.RetrieveUpdateAPIView): # tras os dados e edita.
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "pk" # utilizado para se referir a chave primaria


class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "pk" # utilizado para se referir a chave primaria
