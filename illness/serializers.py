from rest_framework import serializers
from .models import IllnessData
from template.models import SymptomGroup
from template.serializers import SymptomGroupSerializer
from collections import OrderedDict


class IllnessSerializer(serializers.ModelSerializer):
	symptom_groups = SymptomGroupSerializer(read_only=True, many=True)
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
	class Meta:
		model = IllnessData
		exclude = ['id']
		# fields = '__all__'
