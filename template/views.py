from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import SnomedCodeSerializer, LogicalSymptomGroupSerializer, SymptomTemplateSerializer, SymptomCategorySerializer, SymptomGroupSerializer
from .models import SnomedCode, LogicalSymptopGroup, SymptomTemplate, SymptomCategory, SymptomGroup
# Create your views here.
class SnomedCodeView(viewsets.ModelViewSet):
	serializer_class = SnomedCodeSerializer
	queryset = SnomedCode.objects.all()

class LogicalSymptomGroupView(viewsets.ModelViewSet):
	serializer_class = LogicalSymptomGroupSerializer
	queryset = LogicalSymptopGroup.objects.all()

class SymptomTemplateView(viewsets.ModelViewSet):
	serializer_class = SymptomTemplateSerializer
	queryset = SymptomTemplate.objects.all()

class SymptomCategoryView(viewsets.ModelViewSet):
	serializer_class = SymptomCategorySerializer
	queryset = SymptomCategory.objects.all()
	
class SymptomGroupView(viewsets.ModelViewSet):
	serializer_class = SymptomGroupSerializer
	queryset = SymptomGroup.objects.all()
	# def get_queryset(self):
	# 	type_id = self.request.query_params.get('type_id')
	# 	queryset = TreatmentTypeRefModel.objects.filter(id=type_id)
	# 	return queryset