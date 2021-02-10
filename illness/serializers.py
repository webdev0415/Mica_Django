from rest_framework import serializers
from .models import IllnessData
# from template.models import Symptom, SymptomCategory, SymptomGroup, SymptomTmpl, DataStoreSources, Scale, ModifierType, SymptomDataStore
from collections import OrderedDict
# from template.serializers import SymptomGroupSerializer
from template.models import SymptomGroup, Symptom, SymptomCategory
from template.serializers import SymptomDataStoreSerializer, SectionSerializer
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
class SymptomSerializer(serializers.ModelSerializer):
	rows = SymptomDataStoreSerializer(read_only=True, many=True)
	symptomID = serializers.SerializerMethodField()
	displayOrder = serializers.SerializerMethodField()
	genderGroup = serializers.SerializerMethodField()
	@staticmethod
	def setup_eager_loading(queryset):
		queryset = queryset.select_related('symptoms_model')
		queryset = queryset.prefetch_related('rows', 'rows__modifier_values', 'rows__source_info')
		return queryset
	def get_symptomID(self, sample):
		return sample.symtom_id
	def get_displayOrder(self, sample):
		return sample.display_order
	def get_genderGroup(self, sample):
		return sample.gender_group
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = Symptom
		fields = ['symptomID', 'rows', 'displayOrder', 'genderGroup']

class SymptomCategorySerializer(serializers.ModelSerializer):
	symptoms = SymptomSerializer(read_only=True, many=True)
	categoryID = serializers.SerializerMethodField()
	@staticmethod
	def setup_eager_loading(queryset):
		queryset = queryset.prefetch_related('symptoms', 'symptoms__rows', 'symptoms__rows__modifier_values', 'symptoms__rows__source_info')
		return queryset
	def get_categoryID(self, sample):
		return sample.category_id
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = SymptomCategory
		fields = ['categoryID', 'symptoms']

class SymptomGroupSerializer(serializers.ModelSerializer):
	categories = SymptomCategorySerializer(read_only=True, many=True)
	sections = SectionSerializer(read_only=True, many=True)
	groupID = serializers.SerializerMethodField()
	@staticmethod
	def setup_eager_loading(queryset):
		queryset = queryset.prefetch_related('categories', 'categories__symptoms', 'categories__symptoms__symptoms_model', 'categories__symptoms__rows', 'categories__symptoms__rows__modifier_values', 'categories__symptoms__rows__source_info')
		queryset = queryset.prefetch_related('sections', 'sections__categories', 'sections__categories__symptoms', 'sections__categories__symptoms__rows', 'sections__categories__symptoms__rows__modifier_values', 'sections__categories__symptoms__rows__source_info')
		return queryset
	def get_groupID(self, sample):
		return sample.group_id
	def get_updatedDate(self, sample):
		return sample.updated_date
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = SymptomGroup
		fields = ['name', 'groupID', 'categories', 'sections']

class IllnessSerializer(serializers.ModelSerializer):
	symptom_groups = SymptomGroupSerializer(read_only=True, many=True)
	@staticmethod
	def setup_eager_loading(queryset):
		queryset = queryset.prefetch_related('symptom_groups', 'symptom_groups__categories', 'symptom_groups__categories__symptoms', 'symptom_groups__categories__symptoms__symptoms_model', 'symptom_groups__categories__symptoms__rows', 'symptom_groups__categories__symptoms__rows__modifier_values', 'symptom_groups__categories__symptoms__rows__source_info')
		queryset = queryset.prefetch_related('symptom_groups', 'symptom_groups__sections', 'symptom_groups__sections__categories', 'symptom_groups__sections__categories__symptoms', 'symptom_groups__sections__categories__symptoms__symptoms_model', 'symptom_groups__sections__categories__symptoms__rows', 'symptom_groups__sections__categories__symptoms__rows__modifier_values', 'symptom_groups__sections__categories__symptoms__rows__source_info', 'symptom_groups__datastore_ref_types')
		return queryset
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = IllnessData
		exclude = ['id']
		# fields = '__all__'
