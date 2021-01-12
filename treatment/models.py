from django.db import models
import datetime
import uuid
# Create your models here.
class TreatmentTypeRefDesc(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	short_name = models.CharField(max_length=300, null = True, blank = True)
	long_name = models.CharField(max_length=300, null = True, blank = True)
	priority = models.IntegerField(blank=True, null=True)
	default_value = models.BooleanField()
	typedesc_id = models.IntegerField()
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.id
class TreatmentTypeRefModel(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	treatment_type = models.CharField(max_length=300)
	treatment_type_desc = models.ForeignKey(TreatmentTypeRefDesc, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.id