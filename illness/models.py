from django.db import models
import datetime
import uuid
from django.contrib.postgres.fields import ArrayField
from template.models import SymptomGroup, Symptom
# Create your models here.
class IllnessUserData(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	active = models.BooleanField()
	code = models.CharField(max_length=300, null = True, blank = True)
	criticality = models.IntegerField()
	dfstatus = models.CharField(max_length=300, null = True, blank = True)
	es_name = models.CharField(max_length=300, null = True, blank = True)
	groups_complete = ArrayField(
		models.CharField(max_length=300, null = True, blank = True)
		)
	id_icd10_code = models.CharField(max_length=300, null = True, blank = True)
	name = models.CharField(max_length=300, null = True, blank = True)
	rejection_reason = models.CharField(max_length=300, null = True, blank = True)
	source = models.CharField(max_length=300, null = True, blank = True)
	state = models.CharField(max_length=300, null = True, blank = True)
	prevalence = models.IntegerField()
	prior = models.IntegerField()
	user_id = models.IntegerField()
	version = models.IntegerField()
	weight = models.IntegerField()
	symptom_group = models.ForeignKey(SymptomGroup, on_delete=models.CASCADE)
	symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name
class Illness(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	code = models.CharField(max_length=300, null = True, blank = True)
	es_name = models.CharField(max_length=300, null = True, blank = True)
	name = models.CharField(max_length=300, null = True, blank = True)
	user_data = models.ForeignKey(IllnessUserData, on_delete=models.CASCADE)
	def __str__(self):
		return self.name