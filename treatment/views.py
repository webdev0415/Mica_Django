from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import TreatmentTypeRefDescSerializer, TreatmentTypeRefModelSerializer
from .models import TreatmentTypeRefDesc, TreatmentTypeRefModel
from rest_framework.response import Response

class TreatmentTypeRefModelView(viewsets.ModelViewSet):
	serializer_class = TreatmentTypeRefModelSerializer
	queryset = TreatmentTypeRefModel.objects.all()
	def list(self, request, *args, **kwargs):
		qs = self.queryset
		serializer = self.get_serializer(qs, many=True)
		data = {"treatmentTypes": serializer.data}
		return Response(data=data) 