from rest_framework import serializers
from .models import Symptoms, Category, Section, SymptomGroups, ValueStore, DataKeyStore

class ValueStoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = ValueStore
		fields = '__all__'
class DataKeyStoreSerializer(serializers.ModelSerializer):
	values = ValueStoreSerializer()
	class Meta:
		model = DataKeyStore
		fields = '__all__'
class SymptomsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Symptoms
		fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
	symptoms = SymptomsSerializer()
	class Meta:
		model = Category
		fields = '__all__'
class SectionSerializer(serializers.ModelSerializer):
	categories = CategorySerializer()
	class Meta:
		model = Section
		fields = '__all__'
class SymptomGroupsSerializer(serializers.ModelSerializer):
	category = CategorySerializer()
	section = SectionSerializer()
	dataStoreRefTypes = DataKeyStoreSerializer()
	class Meta:
		model = SymptomGroups
		fields = '__all__'

