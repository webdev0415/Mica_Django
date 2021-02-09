from rest_framework import serializers
from .models import DataStoreSources, Scale, ModifierType, SymptomDataStore, SymptomTmpl, Symptom, SymptomCategory, ValueStore, DataKeyStore, SymptomGroup, Section
from collections import OrderedDict
class DataStoreSourcesSerializer(serializers.ModelSerializer):
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = DataStoreSources
		exclude = ['id']
		# fields = '__all__'
class ScaleSerializer(serializers.ModelSerializer):
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = Scale
		exclude = ['id']
class ModifierTypeSerializer(serializers.ModelSerializer):
	scale = ScaleSerializer()
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = ModifierType
		exclude = ['id']

class SymptomDataStoreSerializer(serializers.ModelSerializer):
	modifier_values = ModifierTypeSerializer(read_only=True, many=True)
	source_info = DataStoreSourcesSerializer(read_only=True, many=True)
	@staticmethod
	def setup_eager_loading(queryset):
		queryset = queryset.prefetch_related('modifier_values')
		queryset = queryset.prefetch_related('source_info')
		return queryset
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = SymptomDataStore
		exclude = ['id']
class SymptomTmplSerializer(serializers.ModelSerializer):
	symptomID = serializers.SerializerMethodField()
	rangeValue = serializers.SerializerMethodField()
	def get_symptomID(self, sample):
		return sample.symptom_id

	def get_rangeValue(self, sample):
		return sample.range_values
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = SymptomTmpl
		exclude = ['id', 'symptom_id', 'range_values']
class SymptomSerializer(serializers.ModelSerializer):
	symptoms_model = SymptomTmplSerializer()
	rows = SymptomDataStoreSerializer(read_only=True, many=True)
	@staticmethod
	def setup_eager_loading(queryset):
		queryset = queryset.select_related('symptoms_model')
		queryset = queryset.prefetch_related('rows', 'rows__modifier_values', 'rows__source_info')
		return queryset
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = Symptom
		exclude = ['id']
class SymptomCategorySerializer(serializers.ModelSerializer):
	symptoms = SymptomSerializer(read_only=True, many=True)
	categoryID = serializers.SerializerMethodField()
	@staticmethod
	def setup_eager_loading(queryset):
		queryset = queryset.prefetch_related('symptoms', 'symptoms__symptoms_model', 'symptoms__rows', 'symptoms__rows__modifier_values', 'symptoms__rows__source_info')
		return queryset
	def get_categoryID(self, sample):
		return sample.category_id
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = SymptomCategory
		fields = ['name', 'es_name', 'categoryID', 'symptoms']
		# exclude = ['id']
class ValueStoreSerializer(serializers.ModelSerializer):
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = ValueStore
		exclude = ['id']
class DataKeyStoreSerializer(serializers.ModelSerializer):
	values = ValueStoreSerializer(read_only=True, many=True)
	@staticmethod
	def setup_eager_loading(queryset):
		queryset = queryset.prefetch_related('values')
		return queryset
	def to_representation(self, instance):
		result = super().to_representation(instance)
		response = dict([(key, result[key]) for key in result if result[key] is not None])
		return {f"{instance.name}" :response}
	class Meta:
		model = DataKeyStore
		exclude = ['id', 'name']
class SectionSerializer(serializers.ModelSerializer):
	categories = SymptomCategorySerializer(read_only=True, many=True)
	@staticmethod
	def setup_eager_loading(queryset):
		queryset = queryset.prefetch_related('categories', 'categories__symptoms', 'categories__symptoms__symptoms_model', 'categories__symptoms__rows', 'categories__symptoms__rows__modifier_values', 'categories__symptoms__rows__source_info')
		return queryset
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = Section
		exclude = ['id']
class SymptomGroupSerializer(serializers.ModelSerializer):
	categories = SymptomCategorySerializer(read_only=True, many=True)
	sections = SectionSerializer(read_only=True, many=True)
	dataStoreRefTypes = DataKeyStoreSerializer(read_only=True, many=True, source='datastore_ref_types')
	groupID = serializers.SerializerMethodField()
	updatedDate = serializers.SerializerMethodField()
	@staticmethod
	def setup_eager_loading(queryset):
		queryset = queryset.prefetch_related('categories', 'categories__symptoms', 'categories__symptoms__symptoms_model', 'categories__symptoms__rows', 'categories__symptoms__rows__modifier_values', 'categories__symptoms__rows__source_info')
		queryset = queryset.prefetch_related('sections', 'sections__categories', 'sections__categories__symptoms', 'sections__categories__symptoms__rows', 'sections__categories__symptoms__rows__modifier_values', 'sections__categories__symptoms__rows__source_info')
		queryset = queryset.prefetch_related('datastore_ref_types', 'datastore_ref_types__values')
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
		fields = ['name', 'groupID', 'code', 'updatedDate', 'categories', 'dataStoreRefTypes', 'sections']
		# exclude = ['id']
