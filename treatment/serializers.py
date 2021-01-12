from rest_framework import serializers
from .models import TreatmentTypeRefDesc, TreatmentTypeRefModel

class TreatmentTypeRefDescSerializer(serializers.ModelSerializer):
	class Meta:
		model = TreatmentTypeRefDesc
		fields = '__all__'
class TreatmentTypeRefModelSerializer(serializers.ModelSerializer):
	treatment_type_desc = TreatmentTypeRefDescSerializer()
	class Meta:
		model = TreatmentTypeRefModel
		fields = '__all__'

