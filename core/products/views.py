from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics, permissions

# Views para os produtos

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # nao precisa avisar sobre pk, pois ele ja tem


class ProductEditView(generics.RetrieveUpdateAPIView): # tras os dados e edita.
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "pk" # utilizado para se referir a chave primaria


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "pk" # utilizado para se referir a chave primaria
