from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import TreatmentTypeRefDescSerializer, TreatmentTypeRefModelSerializer
from .models import TreatmentTypeRefDesc, TreatmentTypeRefModel
from rest_framework.response import Response
from django_auto_prefetching import AutoPrefetchViewSetMixin

class TreatmentTypeRefModelView(viewsets.ModelViewSet):
	serializer_class = TreatmentTypeRefModelSerializer
	# queryset = TreatmentTypeRefModel.objects.all()
	def get_queryset(self):
		qs = TreatmentTypeRefModel.objects.all()
		qs = self.get_serializer_class().setup_eager_loading(qs)
		return qs
	def list(self, request, *args, **kwargs):
		qs = self.get_queryset()
		serializer = self.get_serializer(qs, many=True)
		data = {"treatmentTypes": serializer.data}
		return Response(data=data) 