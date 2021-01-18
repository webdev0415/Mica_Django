from rest_framework import serializers
from .models import IllnessUserData, Illness
from template.models import SymptomGroup, Symptom
from template.serializers import SymptomSerializer, SymptomGroupSerializer
class IllnessUserDataSerializer(serializers.ModelSerializer):
	symptom = SymptomSerializer
	symptom_group = SymptomGroupSerializer
	class Meta:
		model = IllnessUserData
		fields = '__all__'
	def create(self, validated_data):
        symptom_data = validated_data.pop('symptom')
        symptop_group_data = validated_data.pop('symptop_group')
        illness_userdata = IllnessUserData.objects.create(**validated_data)
        SymptomGroup.objects.create(illness_userdata=illness_userdata, **symptop_group_data)
        Symptom.objects.create(illness_userdata=illness_userdata, **symptom_data)
        return illness_userdata
    def update(self, instance, validated_data):
    	symptom_data = validated_data.pop('symptom')
        symptop_group_data = validated_data.pop('symptop_group')

    	symptom = instance.symptom
    	symptop_group = instance.symptop_group

    	instance.active = validated_data.get('active', instance.active)
    	instance.code = validated_data.get('code', instance.code)
    	instance.criticality = validated_data.get('criticality', instance.criticality)
    	instance.dfstatus = validated_data.get('dfstatus', instance.dfstatus)
    	instance.es_name = validated_data.get('es_name', instance.es_name)
    	instance.groups_complete = validated_data.get('groups_complete', instance.groups_complete)
    	instance.id_icd10_code = validated_data.get('id_icd10_code', instance.id_icd10_code)
    	instance.name = validated_data.get('name', instance.name)
    	instance.rejection_reason = validated_data.get('rejection_reason', instance.rejection_reason)
    	instance.source = validated_data.get('source', instance.source)
    	instance.state = validated_data.get('state', instance.state)
    	instance.prevalence = validated_data.get('prevalence', instance.prevalence)
    	instance.prior = validated_data.get('prior', instance.prior)
    	instance.user_id = validated_data.get('user_id', instance.user_id)
    	instance.version = validated_data.get('version', instance.version)
    	instance.weight = validated_data.get('weight', instance.weight)
    	instance.save()

    	symptom.name = symptom_data.get('name', symptom.name)
    	symptom.save()

    	symptop_group = symptop_group_data.get('', symptom_group.name)
    	symptom_group.save()
class IllnessSerializer(serializers.ModelSerializer):
	user_data = IllnessUserDataSerializer()
	class Meta:
		model = Illness
		fields = '__all__'
	def create(self, validated_data):
        user_data_content = validated_data.pop('user_data')
        illness = Illness.objects.create(**validated_data)
        IllnessUserData.objects.create(illness=illness, **user_data_content)
        return illness
    def update(self, instance, validated_data):
    	user_data_content = validated_data.pop('user_data')

    	user_data = instance.user_data

    	instance.code = validated_data.get('code', instance.code)
    	instance.es_name = validated_data.get('es_name', instance.es_name)
    	instance.name = validated_data.get('name', instance.name)
    	instance.save()

    	user_data.active = validated_data.get('active', user_data.active)
    	user_data.code = validated_data.get('code', user_data.code)
    	user_data.criticality = validated_data.get('criticality', user_data.criticality)
    	user_data.dfstatus = validated_data.get('dfstatus', user_data.dfstatus)
    	user_data.es_name = validated_data.get('es_name', user_data.es_name)
    	user_data.groups_complete = validated_data.get('groups_complete', user_data.groups_complete)
    	user_data.id_icd10_code = validated_data.get('id_icd10_code', user_data.id_icd10_code)
    	user_data.name = validated_data.get('name', user_data.name)
    	user_data.rejection_reason = validated_data.get('rejection_reason', user_data.rejection_reason)
    	user_data.source = validated_data.get('source', user_data.source)
    	user_data.state = validated_data.get('state', user_data.state)
    	user_data.prevalence = validated_data.get('prevalence', user_data.prevalence)
    	user_data.prior = validated_data.get('prior', user_data.prior)
    	user_data.user_id = validated_data.get('user_id', user_data.user_id)
    	user_data.version = validated_data.get('version', user_data.version)
    	user_data.weight = validated_data.get('weight', user_data.weight)
    	user_data.save()