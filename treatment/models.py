from django.db import models
import datetime
import uuid
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class TreatmentTypeRefDesc(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	code = models.CharField(max_length=300, null = True, blank = True)
	concept_id = ArrayField(
		models.IntegerField()
		)
	cpt_code = ArrayField(
		models.CharField(max_length=300, null = True, blank = True)
		)
	default_value = models.BooleanField()
	es_name = models.CharField(max_length=300, null = True, blank = True)
	description = models.TextField()
	name = models.CharField(max_length=300, null = True, blank = True)
	short_name = models.CharField(max_length=300, null = True, blank = True)
	long_name = models.CharField(max_length=300, null = True, blank = True)
	priority = models.IntegerField(blank=True, null=True)
	typedesc_id = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.id

class TreatmentTypeRefModel(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	code = models.CharField(max_length=300, null = True, blank = True)
	name = models.CharField(max_length=300, null = True, blank = True)
	es_name = models.CharField(max_length=300, null = True, blank = True)
	treatment_type_desc = models.ForeignKey(TreatmentTypeRefDesc, on_delete=models.CASCADE)
	tre_type = models.CharField(max_length=300, null = True, blank = True)
	type_id = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class TreatmentType(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	code = models.CharField(max_length=300, null = True, blank = True)
	name = models.CharField(max_length=300, null = True, blank = True)
	es_name = models.CharField(max_length=300, null = True, blank = True)
	treatment_type = models.ForeignKey(TreatmentTypeRefModel, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name
		