from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import SymptomsSerializer, CategorySerializer, SectionSerializer, SymptomGroupsSerializer
from .models import Symptoms, Category, Section, SymptomGroups
# Create your views here.
class SymptomsView(viewsets.ModelViewSet):
	serializer_class = SymptomsSerializer
	queryset = Symptoms.objects.all()
class CategoryView(viewsets.ModelViewSet):
	serializer_class = CategorySerializer
	queryset = Category.objects.all()
class SectionView(viewsets.ModelViewSet):
	serializer_class = SectionSerializer
	queryset = Section.objects.all()
class SymptomGroupsView(viewsets.ModelViewSet):
	serializer_class = SymptomGroupsSerializer
	queryset = SymptomGroups.objects.all()
	# def get_queryset(self):
	# 	type_id = self.request.query_params.get('type_id')
	# 	queryset = TreatmentTypeRefModel.objects.filter(id=type_id)
	# 	return queryset