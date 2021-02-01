from rest_framework import serializers
# from .models import SnomedCode, LogicalSymptopGroup, RcodeDatastore, SymptomTemplate, SymptomCategory, SymptomGroup, Symptom
from .models import DataStoreSources, Scale, ModifierType, SymptomDataStore, SymptomTmpl, Symptom, SymptomCategory, ValueStore, DataKeyStore, SymptomGroup
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
		# fields = '__all__'
class ModifierTypeSerializer(serializers.ModelSerializer):
	scale = ScaleSerializer()
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = ModifierType
		exclude = ['id']
		# fields = '__all__'

class SymptomDataStoreSerializer(serializers.ModelSerializer):
	modifier_values = ModifierTypeSerializer(read_only=True, many=True)
	source_info = DataStoreSourcesSerializer(read_only=True, many=True)
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = SymptomDataStore
		exclude = ['id']
		# fields = '__all__'
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
		# fields = '__all__'
class SymptomSerializer(serializers.ModelSerializer):
	symptoms_model = SymptomTmplSerializer()
	rows = SymptomDataStoreSerializer(read_only=True, many=True)
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = Symptom
		exclude = ['id']
		# fields = '__all__'
class SymptomCategorySerializer(serializers.ModelSerializer):
	symptoms = SymptomSerializer(read_only=True, many=True)
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = SymptomCategory
		exclude = ['id']
		# fields = '__all__'
class ValueStoreSerializer(serializers.ModelSerializer):
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = ValueStore
		exclude = ['id']
		# fields = '__all__'
class DataKeyStoreSerializer(serializers.ModelSerializer):
	values = ValueStoreSerializer(read_only=True, many=True)
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = DataKeyStore
		exclude = ['id']
		# fields = '__all__'
class SymptomGroupSerializer(serializers.ModelSerializer):
	categories = SymptomCategorySerializer(read_only=True, many=True)
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = SymptomGroup
		exclude = ['id']
		# fields = ['id', 'categories',]
# class SnomedCodeSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = SnomedCode
# 		fields = '__all__'
# class LogicalSymptomGroupSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = LogicalSymptopGroup
# 		fields = '__all__'
# class RcodeDatastoreSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = RcodeDatastore
# 		fields = '__all__'
# class SymptomTemplateSerializer(serializers.ModelSerializer):
# 	# snomed = SnomedCodeSerializer()
# 	# logical = LogicalSymptomGroupSerializer()
# 	class Meta:
# 		model = SymptomTemplate
# 		fields = '__all__'
# 	# def create(self, validated_data):
# 	# 	snomed_data = validated_data.pop('snomed')
# 	# 	logical_data = validated_data.pop('logical')

# 	# 	symptom_template = SymptomTemplate.objects.create(**validated_data)

# 	# 	SnomedCode.objects.create(symptop_category=symptom_category, **snomed_data)
# 	# 	LogicalSymptopGroup.objects.create(symptop_category=symptom_category, **logical_data)
		
# 	# 	return symptom_template
# class SymptomCategorySerializer(serializers.ModelSerializer):
# 	# symptom_template = SymptomTemplateSerializer()
# 	class Meta:
# 		model = SymptomCategory
# 		fields = '__all__'
	# def create(self, validated_data):
	# 	symptomtmpl_data = validated_data.pop('symptom_template')
	# 	symptom_category = SymptomCategory.objects.create(**validated_data)
	# 	SymptomTemplate.objects.create(symptop_category=symptom_category, **symptomtmpl_data)
	# 	return symptop_category
	# def update(self, instance, validated_data):
	# 	symptomtmpl_data = validated_data.pop('symptom_template')

	# 	symptom_template = instance.symptom_template

	# 	instance.name = validated_data.get('name', instance.name)
	# 	instance.parent = validated_data.get('parent', instance.parent)
	# 	instance.code = validated_data.get('code', instance.code)
	# 	instance.bodypart_code = validated_data.get('bodypart_code', instance.bodypart_code)
	# 	instance.es_name = validated_data.get('es_name', instance.es_name)
	# 	instance.cascade_up = validated_data.get('cascade_up', instance.cascade_up)
	# 	instance.cascade_down = validated_data.get('cascade_down', instance.cascade_down)

	# 	instance.save()

	# 	symptom_template.symptom_id = symptomtmpl_data.get('symptom_id', symptom_template.symptom_id)
	# 	symptom_template.criticality = symptomtmpl_data.get('criticality', symptom_template.criticality)
	# 	symptom_template.treatable = symptomtmpl_data.get('treatable', symptom_template.treatable)
	# 	symptom_template.multiple_values = symptomtmpl_data.get('multiple_values', symptom_template.multiple_values)
	# 	symptom_template.code = symptomtmpl_data.get('code', symptom_template.code)
	# 	symptom_template.time_type = symptomtmpl_data.get('time_type', symptom_template.time_type)
	# 	symptom_template.question = symptomtmpl_data.get('question', symptom_template.question)
	# 	symptom_template.icdrcode = symptomtmpl_data.get('icdrcode', symptom_template.icdrcode)
	# 	symptom_template.es_question = symptomtmpl_data.get('es_question', symptom_template.es_question)
	# 	symptom_template.es_question_bk = symptomtmpl_data.get('es_question_bk', symptom_template.es_question_bk)
	# 	symptom_template.name = symptomtmpl_data.get('name', symptom_template.name)
	# 	symptom_template.es_name = symptomtmpl_data.get('es_name', symptom_template.es_name)
	# 	symptom_template.symptom_type = symptomtmpl_data.get('symptom_type', symptom_template.symptom_type)
	# 	symptom_template.px_no_normalized = symptomtmpl_data.get('px_no_normalized', symptom_template.px_no_normalized)
	# 	symptom_template.status = symptomtmpl_data.get('status', symptom_template.status)
	# 	symptom_template.prior = symptomtmpl_data.get('prior', symptom_template.prior)
	# 	symptom_template.sub_groups = symptomtmpl_data.get('sub_groups', symptom_template.sub_groups)
	# 	symptom_template.datastore_templates = symptomtmpl_data.get('datastore_templates', symptom_template.datastore_templates)
	# 	symptom_template.definition = symptomtmpl_data.get('definition', symptom_template.definition)
	# 	symptom_template.painswelling_id = symptomtmpl_data.get('painswelling_id', symptom_template.painswelling_id)
	# 	symptom_template.display_order = symptomtmpl_data.get('display_order', symptom_template.display_order)
	# 	symptom_template.created_at = symptomtmpl_data.get('created_at', symptom_template.created_at)
	# 	symptom_template.updated_at = symptomtmpl_data.get('updated_at', symptom_template.updated_at)
	# 	symptom_template.bias = symptomtmpl_data.get('bias', symptom_template.bias)
	# 	symptom_template.descriptors = symptomtmpl_data.get('descriptors', symptom_template.descriptors)
	# 	symptom_template.descriptor_file = symptomtmpl_data.get('descriptor_file', symptom_template.descriptor_file)
	# 	symptom_template.scaletime_limit = symptomtmpl_data.get('scaletime_limit', symptom_template.scaletime_limit)
	# 	symptom_template.scaletime_limitstart = symptomtmpl_data.get('scaletime_limitstart', symptom_template.scaletime_limitstart)
	# 	symptom_template.timeunit_default = symptomtmpl_data.get('timeunit_default', symptom_template.timeunit_default)
	# 	symptom_template.scaleinfo_text = symptomtmpl_data.get('scaleinfo_text', symptom_template.scaleinfo_text)
	# 	symptom_template.display_symptom = symptomtmpl_data.get('display_symptom', symptom_template.display_symptom)
	# 	symptom_template.kiosk_name = symptomtmpl_data.get('kiosk_name', symptom_template.kiosk_name)
	# 	symptom_template.formal_name = symptomtmpl_data.get('formal_name', symptom_template.formal_name)
	# 	symptom_template.definition = symptomtmpl_data.get('definition', symptom_template.definition)
	# 	symptom_template.med_necessary = symptomtmpl_data.get('med_necessary', symptom_template.med_necessary)
	# 	symptom_template.displaydr_app = symptomtmpl_data.get('displaydr_app', symptom_template.displaydr_app)
	# 	symptom_template.active = symptomtmpl_data.get('active', symptom_template.active)
	# 	symptom_template.gender_group = symptomtmpl_data.get('gender_group', symptom_template.gender_group)
	# 	symptom_template.cardinality = symptomtmpl_data.get('cardinality', symptom_template.cardinality)
	# 	symptom_template.antithesis = symptomtmpl_data.get('antithesis', symptom_template.antithesis)

	# 	symptom_template.save()

	# 	return instance

# class SymptomGroupSerializer(serializers.ModelSerializer):
	# category = SymptomCategorySerializer()
	# class Meta:
	# 	model = SymptomGroup
	# 	fields = '__all__'
	# def create(self, validated_data):
	# 	category_data = validated_data.pop('category')
	# 	symptop_group = SymptomGroup.objects.create(**validated_data)
	# 	SymptomCategory.objects.create(symptop_group=symptop_group, **category_data)
	# 	return symptop_group
	# def update(self, instance, validated_data):
	# 	category_data = validated_data.pop('category')

	# 	category = instance.category

	# 	instance.name = validated_data.get('name', instance.name)
	# 	instance.symptom_count = validated_data.get('symptom_count', instance.symptom_count)
	# 	instance.code = validated_data.get('code', instance.code)
	# 	instance.group_id = validated_data.get('group_id', instance.group_id)
	# 	instance.save()

	# 	category.name = category_data.get('name', category.name)
	# 	category.parent = category_data.get('parent', category.parent)
	# 	category.code = category_data.get('code', category.code)
	# 	category.bodypart_code = category_data.get('bodypart_code', category.bodypart_code)
	# 	category.es_name = category_data.get('es_name', category.es_name)
	# 	category.cascade_up = category_data.get('cascade_up', category.cascade_up)
	# 	category.cascade_down = category_data.get('cascade_down', category.cascade_down)
	# 	category.save()

	# 	return instance
# class SymptomSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Symptom
# 		fields = '__all__'
# class ValueStoreSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = ValueStore
# 		fields = '__all__'
# class DataKeyStoreSerializer(serializers.ModelSerializer):
# 	values = ValueStoreSerializer()
# 	class Meta:
# 		model = DataKeyStore
# 		fields = '__all__'
# 	def create(self, validated_data):
#		 values_data = validated_data.pop('values')
#		 datakeystore = DataKeyStore.objects.create(**validated_data)
#		 DataKeyStore.objects.create(datakeystore=datakeystore, **values_data)
#		 return datakeystore
#	 def update(self, instance, validated_data):
#		 values_data = validated_data.pop('values')
#		 # Unless the application properly enforces that this field is
#		 # always set, the following could raise a `DoesNotExist`, which
#		 # would need to be handled.
#		 values = instance.values
#		 instance.title = validated_data.get('title', instance.title)
#		 instance.es_title = validated_data.get('es_title', instance.es_title)
#		 instance.save()

#		 values.m_antithesis = values_data.get(
#			 'm_antithesis',
#			 values.m_antithesis
#		 )
#		 values.m_icd10Rcode = values_data.get(
#			 'm_icd10Rcode',
#			 values.m_icd10Rcode
#		 )
#		 values.count = values_data.get(
#			 'count',
#			 values.count
#		 )
#		 values.displayListValue = values_data.get(
#			 'displayListValue',
#			 values.displayListValue
#		 )
#		 values.kiosk_name = values_data.get(
#			 'kiosk_name',
#			 values.kiosk_name
#		 )
#		 values.es_kiosk_name = values_data.get(
#			 'es_kiosk_name',
#			 values.es_kiosk_name
#		 )
#		 values.display_order = values_data.get(
#			 'display_order',
#			 values.display_order
#		 )
#		 values.save()
#		 return instance


# class CategorySerializer(serializers.ModelSerializer):
# 	symptoms = SymptomSerializer()
# 	class Meta:
# 		model = Category
# 		fields = '__all__'
# 	def create(self, validated_data):
#		 symptoms_data = validated_data.pop('symptoms')
#		 category = DataKeyStore.objects.create(**validated_data)
#		 DataKeyStore.objects.create(category=category, **symptoms_data)
#		 return category
#	 def update(self, instance, validated_data):
#		 symptoms_data = validated_data.pop('symptoms')
#		 # Unless the application properly enforces that this field is
#		 # always set, the following could raise a `DoesNotExist`, which
#		 # would need to be handled.
#		 symptoms = instance.symptoms
#		 instance.category_name = validated_data.get('category_name', instance.category_name)
#		 instance.save()

#		 symptoms.multiple_values = values_data.get(
#			 'multiple_values',
#			 values.multiple_values
#		 )
		
#		 values.save()
#		 return instance
# class SectionSerializer(serializers.ModelSerializer):
# 	categories = CategorySerializer()
# 	class Meta:
# 		model = Section
# 		fields = '__all__'
# 	def create(self, validated_data):
#		 categories_data = validated_data.pop('categories')
#		 section = Section.objects.create(**validated_data)
#		 DataKeyStore.objects.create(section=section, **categories_data)
#		 return section
# class SymptomGroupSerializer(serializers.ModelSerializer):
# 	category = CategorySerializer()
# 	section = SectionSerializer()
# 	dataStoreRefTypes = DataKeyStoreSerializer()
# 	class Meta:
# 		model = SymptomGroup
# 		fields = '__all__'
# 	def create(self, validated_data):
#		 category_data = validated_data.pop('category')
#		 section_data = validated_data.pop('section')
#		 dataStoreRefTypes_data = validated_data.pop('dataStoreRefTypes')
#		 symptomgroup = SymptomGroup.objects.create(**validated_data)
#		 SymptomGroup.objects.create(symptomgroup=symptomgroup, **categories_data, **section_data, **dataStoreRefTypes_data)
#		 return section

