from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import IllnessSerializer
from .models import IllnessData
from rest_framework import generics
from rest_framework.response import Response
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
# class IllnessDataView(viewsets.ModelViewSet):
# 	serializer_class = IllnessSerializer
# 	queryset = IllnessData.objects.all()
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