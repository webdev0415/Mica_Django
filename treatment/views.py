from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import TreatmentTypeRefDescSerializer, TreatmentTypeRefModelSerializer, TreatmentTypeSerializer
from .models import TreatmentTypeRefDesc, TreatmentTypeRefModel, TreatmentType
# Create your views here.
class TreatmentTypeRefDescView(viewsets.ModelViewSet):
	serializer_class = TreatmentTypeRefDescSerializer
	queryset = TreatmentTypeRefDesc.objects.all()

class TreatmentTypeRefModelView(viewsets.ModelViewSet):
	serializer_class = TreatmentTypeRefModelSerializer
	queryset = TreatmentTypeRefModel.objects.all()

	# def get_queryset(self):
	# 	type_id = self.request.query_params.get('type_id')
	# 	queryset = TreatmentTypeRefModel.objects.filter(id=type_id)
	# 	return queryset
class TreatmentTypeView(viewsets.ModelViewSet):
	serializer_class = TreatmentTypeSerializer
	queryset = TreatmentType.objects.all()