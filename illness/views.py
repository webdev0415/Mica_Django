from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import IllnessSerializer
from .models import IllnessData
from rest_framework import generics
from rest_framework.response import Response

from rest_framework.filters import SearchFilter
from url_filter.integrations.drf import DjangoFilterBackend

# Create your views here.
# class CategoryView(viewsets.ModelViewSet):
# 	serializer_class = CategorySerializer
# 	queryset = Category.objects.all()
class IllnessListView(generics.ListAPIView):
	serializer_class = IllnessSerializer
	# queryset = IllnessData.objects.all()
	# lookup_field = "icd10_code"
	def get_queryset(self):
		
		icd10_code = self.kwargs['icd10_code']
		queryset = IllnessData.objects.filter(icd10_code=icd10_code).distinct()
		# serializer = IllnessSerializer()
		return queryset
class IllnessCreateView(generics.CreateAPIView):
    serializer_class = IllnessSerializer

class IllnessDataViewSet(viewsets.ModelViewSet):
	queryset = IllnessData.objects.all()	
	serializer_class = IllnessSerializer
	lookup_field = "icd10_code"
	# lookup_url_kwarg = "icd10_code"
	filter_backends = [DjangoFilterBackend, SearchFilter]
	filter_fields = [field.name for field in IllnessData._meta.fields]
	search_fields = ["icd10_code", "verison", "state"]

class IllnessUpdateView(generics.RetrieveUpdateAPIView):
	lookup_url_kwarg = "icd10_code"
	lookup_field = "icd10_code"
	serializer_class = IllnessSerializer
	
	def get_queryset(self):
		icd10_code = self.kwargs['icd10_code']
		queryset = IllnessData.objects.filter(icd10_code=icd10_code)
		return queryset
	# def get_queryset(self):
	# 	print("->", self.request)

	# def get_queryset(self):
	# 	icd10_code = self.request.query_params.get('icd10_code')
	# 	print("====================>", self.request.query_params)
	# 	queryset = IllnessData.objects.filter(icd10_code=icd10_code)
	# 	return queryset