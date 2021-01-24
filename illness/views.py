from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import CategorySerializer, IllnessSerializer
from .models import Category, IllnessData
# Create your views here.
class CategoryView(viewsets.ModelViewSet):
	serializer_class = CategorySerializer
	queryset = Category.objects.all()
class IllnessView(viewsets.ModelViewSet):
	serializer_class = IllnessSerializer
	queryset = IllnessData.objects.all()