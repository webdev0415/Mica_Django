from rest_framework import serializers
from .models import Symptom, Category, Section, SymptomGroup, ValueStore, DataKeyStore, SnomedCode, LogicalSymptopGroup, SymptomTemplate, SymptomCategory, SymptomGroup

class SnomedCodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = ValueStore
		fields = '__all__'
class LogicalSymptopGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = ValueStore
		fields = '__all__'
class SymptomTemplateSerializer(serializers.ModelSerializer):
	class Meta:
		model = ValueStore
		fields = '__all__'
class SymptomCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = ValueStore
		fields = '__all__'
class SymptomGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = ValueStore
		fields = '__all__'

class ValueStoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = ValueStore
		fields = '__all__'
class DataKeyStoreSerializer(serializers.ModelSerializer):
	values = ValueStoreSerializer()
	class Meta:
		model = DataKeyStore
		fields = '__all__'
	def create(self, validated_data):
        values_data = validated_data.pop('values')
        datakeystore = DataKeyStore.objects.create(**validated_data)
        DataKeyStore.objects.create(datakeystore=datakeystore, **values_data)
        return datakeystore
    def update(self, instance, validated_data):
        values_data = validated_data.pop('values')
        # Unless the application properly enforces that this field is
        # always set, the following could raise a `DoesNotExist`, which
        # would need to be handled.
        values = instance.values
        instance.title = validated_data.get('title', instance.title)
        instance.es_title = validated_data.get('es_title', instance.es_title)
        instance.save()

        values.m_antithesis = values_data.get(
            'm_antithesis',
            values.m_antithesis
        )
        values.m_icd10Rcode = values_data.get(
            'm_icd10Rcode',
            values.m_icd10Rcode
        )
        values.count = values_data.get(
            'count',
            values.count
        )
        values.displayListValue = values_data.get(
            'displayListValue',
            values.displayListValue
        )
        values.kiosk_name = values_data.get(
            'kiosk_name',
            values.kiosk_name
        )
        values.es_kiosk_name = values_data.get(
            'es_kiosk_name',
            values.es_kiosk_name
        )
        values.display_order = values_data.get(
            'display_order',
            values.display_order
        )
        values.save()
        return instance

class SymptomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Symptom
		fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
	symptoms = SymptomSerializer()
	class Meta:
		model = Category
		fields = '__all__'
	def create(self, validated_data):
        symptoms_data = validated_data.pop('symptoms')
        category = DataKeyStore.objects.create(**validated_data)
        DataKeyStore.objects.create(category=category, **symptoms_data)
        return category
    def update(self, instance, validated_data):
        symptoms_data = validated_data.pop('symptoms')
        # Unless the application properly enforces that this field is
        # always set, the following could raise a `DoesNotExist`, which
        # would need to be handled.
        symptoms = instance.symptoms
        instance.category_name = validated_data.get('category_name', instance.category_name)
        instance.save()

        symptoms.multiple_values = values_data.get(
            'multiple_values',
            values.multiple_values
        )
        
        values.save()
        return instance
class SectionSerializer(serializers.ModelSerializer):
	categories = CategorySerializer()
	class Meta:
		model = Section
		fields = '__all__'
	def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        section = Section.objects.create(**validated_data)
        DataKeyStore.objects.create(section=section, **categories_data)
        return section
class SymptomGroupSerializer(serializers.ModelSerializer):
	category = CategorySerializer()
	section = SectionSerializer()
	dataStoreRefTypes = DataKeyStoreSerializer()
	class Meta:
		model = SymptomGroup
		fields = '__all__'
	def create(self, validated_data):
        category_data = validated_data.pop('category')
        section_data = validated_data.pop('section')
        dataStoreRefTypes_data = validated_data.pop('dataStoreRefTypes')
        symptomgroup = SymptomGroup.objects.create(**validated_data)
        SymptomGroup.objects.create(symptomgroup=symptomgroup, **categories_data, **section_data, **dataStoreRefTypes_data)
        return section

