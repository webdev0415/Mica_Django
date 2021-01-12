from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import BodyPartSerializer
from .models import BodyParts
# Create your views here.
class BodyPartsView(viewsets.ModelViewSet):
	serializer_class = BodyPartSerializer
	queryset = BodyParts.objects.all()