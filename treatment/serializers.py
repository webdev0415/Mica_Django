from rest_framework import serializers
from .models import TreatmentTypeRefDesc, TreatmentTypeRefModel
from collections import OrderedDict

class TreatmentTypeRefDescSerializer(serializers.ModelSerializer):
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = TreatmentTypeRefDesc
		exclude = ['id']
		# fields = '__all__'

class TreatmentTypeRefModelSerializer(serializers.ModelSerializer):
	# treatment_type_desc = TreatmentTypeRefDescSerializer(read_only=True, many=True)
	treatmentTypeDesc = TreatmentTypeRefDescSerializer(read_only=True, many=True, source='treatment_type_desc')
	typeID = serializers.SerializerMethodField()
	types = serializers.SerializerMethodField()
	@staticmethod
	def setup_eager_loading(queryset):
		queryset = queryset.prefetch_related('treatment_type_desc')
		return queryset
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	def get_typeID(self, sample):
		return sample.type_id
	def get_types(self, sample):
		return sample.tre_type
	class Meta:
		model = TreatmentTypeRefModel
		# exclude = ['id', 'tre_type']
		fields = ['typeID', 'types', 'name', 'active', 'treatmentTypeDesc']
		# fields = '__all__'


