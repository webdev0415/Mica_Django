from rest_framework import serializers
from .models import Drug, NonDrug, TreatmentGroup, Treatment

class DrugSerializer(serializers.ModelSerializer):
	class Meta:
		model = Drug
		fields = '__all__'
class NonDrugSerializer(serializers.ModelSerializer):
	class Meta:
		model = NonDrug
		fields = '__all__'
class TreatmentGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = TreatmentGroup
		fields = '__all__'
class TreatmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Treatment
		fields = '__all__'
# class TreatmentTypeRefModelSerializer(serializers.ModelSerializer):
# 	treatment_type_desc = TreatmentTypeRefDescSerializer()
# 	class Meta:
# 		model = TreatmentTypeRefModel
# 		fields = '__all__'
# 	def create(self, validated_data):
# 		treatment_type_desc_data = validated_data.pop('treatment_type_desc')
# 		treatment_type = TreatmentTypeRefModel.objects.create(**validated_data)
# 		TreatmentTypeRefDesc.objects.create(treatment_type=treatment_type, **treatment_type_desc_data)
# 		return treatment_type
# 	def update(self, instance, validated_data):
# 		treatment_type_desc_data = validated_data.pop('treatment_type_desc')

# 		treatment_type_desc = instance.treatment_type_desc

# 		instance.name = validated_data.get('name', instance.name)
# 		instance.es_name = validated_data.get('es_name', instance.es_name)
# 		instance.code = validated_data.get('code', instance.code)
# 		instance.tre_type = validated_data.get('tre_type', instance.tre_type)
# 		instance.type_id = validated_data.get('type_id', instance.type_id)
# 		instance.save()

# 		treatment_type_desc.name = treatment_type_desc_data.get('name', treatment_type_desc.name)
# 		treatment_type_desc.concept_id = treatment_type_desc_data.get('concept_id', treatment_type_desc.concept_id)
# 		treatment_type_desc.code = treatment_type_desc_data.get('code', treatment_type_desc.code)
# 		treatment_type_desc.cpt_code = treatment_type_desc_data.get('cpt_code', treatment_type_desc.cpt_code)
# 		treatment_type_desc.es_name = treatment_type_desc_data.get('es_name', treatment_type_desc.es_name)
# 		treatment_type_desc.default_value = treatment_type_desc_data.get('default_value', treatment_type_desc.default_value)
# 		treatment_type_desc.description = treatment_type_desc_data.get('description', treatment_type_desc.description)
# 		treatment_type_desc.short_name = treatment_type_desc_data.get('short_name', treatment_type_desc.short_name)
# 		treatment_type_desc.long_name = treatment_type_desc_data.get('long_name', treatment_type_desc.long_name)
# 		treatment_type_desc.priority = treatment_type_desc_data.get('priority', treatment_type_desc.priority)
# 		treatment_type_desc.typedesc_id = treatment_type_desc_data.get('typedesc_id', treatment_type_desc.typedesc_id)
# 		treatment_type_desc.save()

# 		return instance

# class TreatmentTypeSerializer(serializers.ModelSerializer):
# 	treatment_type = TreatmentTypeRefModelSerializer()
# 	class Meta:
# 		model = TreatmentType
# 		fields = '__all__'
# 	def create(self, validated_data):
# 		treatment_type_data = validated_data.pop('treatment_type')
# 		treatment = TreatmentType.objects.create(**validated_data)
# 		TreatmentTypeRefModel.objects.create(treatment=treatment, **treatment_type_data)
# 		return treatment
# 	def update(self, instance, validated_data):
# 		treatment_type_data = validated_data.pop('treatment_type')

# 		treatment_type = instance.treatment_type

# 		instance.name = validated_data.get('name', instance.name)
# 		instance.es_name = validated_data.get('es_name', instance.es_name)
# 		instance.code = validated_data.get('code', instance.code)
# 		instance.save()

# 		treatment_type.name = treatment_type_data.get('name', treatment_type.name)
# 		treatment_type.code = treatment_type_data.get('code', treatment_type.code)
# 		treatment_type.es_name = treatment_type_data.get('es_name', treatment_type.es_name)
# 		treatment_type.tre_type = treatment_type_data.get('tre_type', treatment_type.tre_type)
# 		treatment_type.type_id = treatment_type_data.get('type_id', treatment_type.type_id)

# 		treatment_type.save()

# 		return instance

