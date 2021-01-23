from django.shortcuts import render
from rest_framework import viewsets 
# from .serializers import TreatmentTypeRefDescSerializer, TreatmentTypeRefModelSerializer, TreatmentTypeSerializer
# from .models import TreatmentTypeRefDesc, TreatmentTypeRefModel, TreatmentType
from .serializers import DrugSerializer, NonDrugSerializer, TreatmentGroupSerializer, TreatmentSerializer
from .models import Drug, NonDrug, TreatmentGroup, Treatment

class DrugView(viewsets.ModelViewSet):
	serializer_class = DrugSerializer
	queryset = Drug.objects.all()

class NonDrugView(viewsets.ModelViewSet):
	serializer_class = NonDrugSerializer
	queryset = NonDrug.objects.all()

class TreatmentGroupView(viewsets.ModelViewSet):
	serializer_class = TreatmentGroupSerializer
	queryset = TreatmentGroup.objects.all()

class TreatmentView(viewsets.ModelViewSet):
	serializer_class = TreatmentSerializer
	queryset = Treatment.objects.all()
# Create your views here.
# class TreatmentTypeRefDescView(viewsets.ModelViewSet):
# 	serializer_class = TreatmentTypeRefDescSerializer
# 	queryset = TreatmentTypeRefDesc.objects.all()

# class TreatmentTypeRefModelView(viewsets.ModelViewSet):
# 	serializer_class = TreatmentTypeRefModelSerializer
# 	queryset = TreatmentTypeRefModel.objects.all()

	# def get_queryset(self):
	# 	type_id = self.request.query_params.get('type_id')
	# 	queryset = TreatmentTypeRefModel.objects.filter(id=type_id)
	# 	return queryset
# class TreatmentTypeView(viewsets.ModelViewSet):
# 	serializer_class = TreatmentTypeSerializer
# 	queryset = TreatmentType.objects.all()