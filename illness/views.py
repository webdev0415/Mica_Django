from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import IllnessSerializer
from .models import IllnessData
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from url_filter.integrations.drf import DjangoFilterBackend


# class IllnessListView(generics.ListAPIView):
# 	serializer_class = IllnessSerializer
# 	def get_queryset(self):
		
# 		icd10_code = self.kwargs['icd10_code']
# 		queryset = IllnessData.objects.filter(icd10_code=icd10_code).distinct()
# 		return queryset

# class IllnessCreateView(generics.CreateAPIView):
#     serializer_class = IllnessSerializer


class IllnessDataView(viewsets.ModelViewSet):
	# queryset = IllnessData.objects.all()	
	serializer_class = IllnessSerializer
	lookup_field = "icd10_code"
	lookup_url_kwarg = "icd10_code"
	filter_backends = [DjangoFilterBackend]
	filterset_fields = [ "verison", "state"]
	filter_fields = [field.name for field in IllnessData._meta.fields]
	search_fields = [ "icd10_code", "verison", "state"]
	lookup_value_regex = '[\w\.]+'

	def get_queryset(self):
		if 'icd10_code' in self.kwargs:
			return IllnessData.objects.filter(icd10_code=self.kwargs['icd10_code'])
		else:
			return IllnessData.objects.all()

	def retrieve(self, request, *args, **kwargs):
		state =  request.GET.get('state', None)
		version = request.GET.get("version" or None)
		qs = self.get_queryset()	
		if version and state:
			qs = qs.filter(version=version, state=state)
		elif version and not state:
			qs = qs.filter(version=version)
		elif state and not version:
			qs = qs.filter(state=state)
		
		serializer = self.get_serializer(qs, many=True)
		data = {"userData": serializer.data}
		return Response(data=data)
