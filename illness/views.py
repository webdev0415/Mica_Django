from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import IllnessUserDataSerializer, IllnessSerializer
from .model import IllnessUserData, Illness
# Create your views here.
class IllnessUserDataView(viewsets.ModelViewSet):
	serializer_class = IllnessUserDataSerializer
	queryset = IllnessUserData.objects.all()
class IllnessView(viewsets.ModelViewSet):
	serializer_class = IllnessSerializer
	queryset = Illness.objects.all()