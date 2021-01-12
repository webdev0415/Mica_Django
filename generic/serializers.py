from rest_framework import serializers
from .models import BodyParts

class BodyPartSerializer(serializers.ModelSerializer):
	class Meta:
		model = BodyParts
		fields = '__all__'