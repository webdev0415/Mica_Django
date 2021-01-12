from rest_framework import serializers
from .models import BodyPart

class BodyPartSerializer(serializers.ModelSerializer):
	class Meta:
		model = BodyPart
		fields = '__all__'