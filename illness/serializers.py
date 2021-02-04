from rest_framework import serializers
from .models import IllnessData
# from template.models import Symptom, SymptomCategory, SymptomGroup, SymptomTmpl, DataStoreSources, Scale, ModifierType, SymptomDataStore
from collections import OrderedDict
from template.serializers import SymptomGroupSerializer
# class DataStoreSourcesSerializer(serializers.ModelSerializer):
# 	def to_representation(self, instance):
# 		result = super().to_representation(instance)
# 		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
# 	class Meta:
# 		model = DataStoreSources
# 		exclude = ['id']
# 		# fields = '__all__'
# class ScaleSerializer(serializers.ModelSerializer):
# 	def to_representation(self, instance):
# 		result = super().to_representation(instance)
# 		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
# 	class Meta:
# 		model = Scale
# 		exclude = ['id']
# 		# fields = '__all__'
# class ModifierTypeSerializer(serializers.ModelSerializer):
# 	scale = ScaleSerializer()
# 	def to_representation(self, instance):
# 		result = super().to_representation(instance)
# 		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
# 	class Meta:
# 		model = ModifierType
# 		exclude = ['id']
# 		# fields = '__all__'

# class SymptomDataStoreSerializer(serializers.ModelSerializer):
# 	modifier_values = ModifierTypeSerializer(read_only=True, many=True)
# 	source_info = DataStoreSourcesSerializer(read_only=True, many=True)
# 	def to_representation(self, instance):
# 		result = super().to_representation(instance)
# 		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
# 	class Meta:
# 		model = SymptomDataStore
# 		exclude = ['id']

# class SymptomTmplSerializer(serializers.ModelSerializer):
# 	symptomID = serializers.SerializerMethodField()
# 	rangeValue = serializers.SerializerMethodField()
# 	def get_symptomID(self, sample):
# 		return sample.symptom_id

# 	def get_rangeValue(self, sample):
# 		return sample.range_values
# 	def to_representation(self, instance):
# 		result = super().to_representation(instance)
# 		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
# 	class Meta:
# 		model = SymptomTmpl
# 		exclude = ['id', 'symptom_id', 'range_values']

# class SymptomSerializer(serializers.ModelSerializer):
# 	symptoms_model = SymptomTmplSerializer()
# 	rows = SymptomDataStoreSerializer(read_only=True, many=True)
# 	def to_representation(self, instance):
# 		result = super().to_representation(instance)
# 		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
# 	class Meta:
# 		model = Symptom
# 		exclude = ['id']
# 		# fields = '__all__'

# class SymptomCategorySerializer(serializers.ModelSerializer):
# 	symptoms = SymptomSerializer(read_only=True, many=True)
# 	def to_representation(self, instance):
# 		result = super().to_representation(instance)
# 		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
# 	class Meta:
# 		model = SymptomCategory
# 		exclude = ['id']

# class SymptomGroupSerializer(serializers.ModelSerializer):
# 	categories = SymptomCategorySerializer(read_only=True, many=True)
# 	def to_representation(self, instance):
# 		result = super().to_representation(instance)
# 		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
# 	class Meta:
# 		model = SymptomGroup
# 		exclude = ['id']

class IllnessSerializer(serializers.ModelSerializer):
	symptom_groups = SymptomGroupSerializer(read_only=True, many=True)
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = IllnessData
		exclude = ['id']
		# fields = '__all__'
