from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SymptomGroupSerializer, SymptomCategorySerializer, DataKeyStoreSerializer
from .models import SymptomGroup, SymptomCategory, DataKeyStore
from rest_framework.response import Response
from django_auto_prefetching import AutoPrefetchViewSetMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.decorators import api_view
# from .serializers import SnomedCodeSerializer, LogicalSymptomGroupSerializer, SymptomTemplateSerializer, SymptomCategorySerializer, SymptomGroupSerializer
# from .models import SnomedCode, LogicalSymptopGroup, SymptomTemplate, SymptomCategory, SymptomGroup
# Create your views here.
# class SnomedCodeView(viewsets.ModelViewSet):
# 	serializer_class = SnomedCodeSerializer
# 	queryset = SnomedCode.objects.all()

class SymptomCategoryView(viewsets.ModelViewSet):
	queryset = SymptomCategory.objects.all()
	serializer_class = SymptomCategorySerializer

class DataKeyStoreView(viewsets.ModelViewSet):
	queryset = DataKeyStore.objects.all()
	serializer_class = DataKeyStoreSerializer

class SymptomGroupView(viewsets.ModelViewSet):
	serializer_class = SymptomGroupSerializer
	
	def get_queryset(self):
		qs = SymptomGroup.objects.all()
		qs = self.get_serializer_class().setup_eager_loading(qs)
		return qs
	# @method_decorator(cache_page(60))
	# @method_decorator(vary_on_cookie)
	def list(self, request, *args, **kwargs):
		qs = self.get_queryset()
		serializer = self.get_serializer(qs, many=True)
		data = {"symptomGroups": serializer.data}
		return Response(data=data)
	# serializer_class = SymptomGroupSerializer
	# queryset = SymptomGroup.objects.all()
	# def list(self, request, *args, **kwargs):
	# 	qs = self.queryset
	# 	serializer = self.get_serializer(qs, many=True)
	# 	data = {"symptomGroups": serializer.data}
	# 	return Response(data=data)
	
# class LogicalSymptomGroupView(viewsets.ModelViewSet):
# 	serializer_class = LogicalSymptomGroupSerializer
# 	queryset = LogicalSymptopGroup.objects.all()

# class SymptomTemplateView(viewsets.ModelViewSet):
# 	serializer_class = SymptomTemplateSerializer
# 	queryset = SymptomTemplate.objects.all()

# class SymptomCategoryView(viewsets.ModelViewSet):
# 	serializer_class = SymptomCategorySerializer
# 	queryset = SymptomCategory.objects.all()
	
# class SymptomGroupView(viewsets.ModelViewSet):
# 	serializer_class = SymptomGroupSerializer
# 	queryset = SymptomGroup.objects.all()
	# def get_queryset(self):
	# 	type_id = self.request.query_params.get('type_id')
	# 	queryset = TreatmentTypeRefModel.objects.filter(id=type_id)
	# 	return queryset