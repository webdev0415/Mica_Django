from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import SymptomSerializer, CategorySerializer, SectionSerializer, SymptomGroupSerializer
from .models import Symptom, Category, Section, SymptomGroup
# Create your views here.
class SymptomView(viewsets.ModelViewSet):
	serializer_class = SymptomSerializer
	queryset = Symptom.objects.all()
class CategoryView(viewsets.ModelViewSet):
	serializer_class = CategorySerializer
	queryset = Category.objects.all()
class SectionView(viewsets.ModelViewSet):
	serializer_class = SectionSerializer
	queryset = Section.objects.all()
class SymptomGroupView(viewsets.ModelViewSet):
	serializer_class = SymptomGroupSerializer
	queryset = SymptomGroup.objects.all()
	# def get_queryset(self):
	# 	type_id = self.request.query_params.get('type_id')
	# 	queryset = TreatmentTypeRefModel.objects.filter(id=type_id)
	# 	return queryset