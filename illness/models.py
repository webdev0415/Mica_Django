from django.db import models
import datetime
import uuid
from django.contrib.postgres.fields import ArrayField
from template.models import SymptomGroup
# from template.models import SymptomGroup, Symptom
# Create your models here.
# class IllnessUserData(models.Model):
# 	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
# 	active = models.BooleanField()
# 	code = models.CharField(max_length=300, null = True, blank = True)
# 	criticality = models.IntegerField()
# 	dfstatus = models.CharField(max_length=300, null = True, blank = True)
# 	es_name = models.CharField(max_length=300, null = True, blank = True)
# 	groups_complete = ArrayField(
# 		models.CharField(max_length=300, null = True, blank = True)
# 		)
# 	id_icd10_code = models.CharField(max_length=300, null = True, blank = True)
# 	name = models.CharField(max_length=300, null = True, blank = True)
# 	rejection_reason = models.CharField(max_length=300, null = True, blank = True)
# 	source = models.CharField(max_length=300, null = True, blank = True)
# 	state = models.CharField(max_length=300, null = True, blank = True)
# 	prevalence = models.IntegerField()
# 	prior = models.IntegerField()
# 	user_id = models.IntegerField()
# 	version = models.IntegerField()
# 	weight = models.IntegerField()
# 	symptom_group = models.ForeignKey(SymptomGroup, on_delete=models.CASCADE)
# 	symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
# 	created_at = models.DateTimeField(auto_now_add=True, editable=False)
# 	updated_at = models.DateTimeField(auto_now=True)
# 	def __str__(self):
# 		return self.name



class IllnessData(models.Model):
	icd10_code = models.CharField(max_length=300, null = True, blank = True)
	cluster = models.IntegerField(null = True)
	criticality = models.IntegerField(null = True)
	active = models.BooleanField(null = True)
	dfstatus = models.CharField(max_length=300, null = True, blank = True)
	source = models.CharField(max_length=300, null = True, blank = True)
	groups_complete = ArrayField(
		models.CharField(max_length=300, null = True, blank = True)
		)
	version = models.IntegerField(null = True)
	prevalence = models.IntegerField(null = True)
	prior = models.FloatField(null = True)
	name = models.CharField(max_length=300, null = True, blank = True)
	mergedversions = models.CharField(max_length=300, null = True, blank = True)
	state = models.CharField(max_length=300, null = True, blank = True)
	symptom_groups = models.ManyToManyField(SymptomGroup, related_name='illness_symptomgroup', blank=True)
	created_at = models.DateTimeField(auto_now_add=True, editable=False, null = True)
	updated_at = models.DateTimeField(auto_now=True, null = True)
	# categories = ArrayField(
	# 	models.IntegerField()
	# 	)
	# categories = models.ManyToManyField(Category, related_name='illness_category')
	def __str__(self):
		return self.name