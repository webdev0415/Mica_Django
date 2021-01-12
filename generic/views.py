from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import BodyPartSerializer
from .models import BodyPart
# Create your views here.
class BodyPartView(viewsets.ModelViewSet):
	serializer_class = BodyPartSerializer
	queryset = BodyPart.objects.all()