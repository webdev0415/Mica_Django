from rest_framework import serializers
from .models import Symptom, Category, Section, SymptomGroup, ValueStore, DataKeyStore

class ValueStoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = ValueStore
		fields = '__all__'
class DataKeyStoreSerializer(serializers.ModelSerializer):
	values = ValueStoreSerializer()
	class Meta:
		model = DataKeyStore
		fields = '__all__'
class SymptomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Symptom
		fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
	symptoms = SymptomSerializer()
	class Meta:
		model = Category
		fields = '__all__'
class SectionSerializer(serializers.ModelSerializer):
	categories = CategorySerializer()
	class Meta:
		model = Section
		fields = '__all__'
class SymptomGroupSerializer(serializers.ModelSerializer):
	category = CategorySerializer()
	section = SectionSerializer()
	dataStoreRefTypes = DataKeyStoreSerializer()
	class Meta:
		model = SymptomGroup
		fields = '__all__'

