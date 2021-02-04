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
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = Symptom
		exclude = ['id']
class SymptomCategorySerializer(serializers.ModelSerializer):
	symptoms = SymptomSerializer(read_only=True, many=True)
	categoryID = serializers.SerializerMethodField()
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
	def to_representation(self, instance):
		result = super().to_representation(instance)
		result = dict([(key, result[key]) for key in result if result[key] is not None])
		return {f"{instance.name}" :result}
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = DataKeyStore
		exclude = ['id', 'name']
class SectionSerializer(serializers.ModelSerializer):
	categories = SymptomCategorySerializer(read_only=True, many=True)
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
