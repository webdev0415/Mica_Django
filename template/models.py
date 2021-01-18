from django.db import models
import datetime
import uuid
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class SnomedCode(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	code = models.CharField(max_length=300, null = True, blank = True)
	name = models.CharField(max_length=300, null = True, blank = True)
	concept_id = ArrayField(
		models.BigIntegerField(),
		)
	expression = models.CharField(max_length=300, null = True, blank = True)
	list_valuecode = models.CharField(max_length=300, null = True, blank = True)
	list_value = models.CharField(max_length=300, null = True, blank = True)
	def __str__(self):
		return self.name
class LogicalSymptopGroup(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	group_id = models.IntegerField()
	group_lag = models.IntegerField()
class SymptomTemplate(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	symptom_id = models.CharField(max_length=300, null = True, blank = True)
	criticality = models.IntegerField()
	treatable = models.BooleanField()
	multiple_values = models.CharField(max_length=300, null = True, blank = True)
	code = models.CharField(max_length=300, null = True, blank = True)
	time_type = models.CharField(max_length=300, null = True, blank = True)
	question = models.CharField(max_length=300, null = True, blank = True)
	icdrcode = models.CharField(max_length=300, null = True, blank = True)
	es_question = models.CharField(max_length=300, null = True, blank = True)
	es_question_bk = models.CharField(max_length=300, null = True, blank = True)
	name = models.CharField(max_length=300, null = True, blank = True)
	es_name = models.CharField(max_length=300, null = True, blank = True)
	symptom_type = models.CharField(max_length=300, null = True, blank = True)
	px_no_normalized = models.FloatField()
	status = models.CharField(max_length=300, null = True, blank = True)
	prior = models.FloatField()
	sub_groups = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	datastore_templates = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	definition = models.CharField(max_length=300, null = True, blank = True)
	painswelling_id = models.IntegerField()
	display_order = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True)
	bias = models.BooleanField()
	descriptors = models.CharField(max_length=300, null = True, blank = True)
	descriptor_file = models.CharField(max_length=300, null = True, blank = True)
	scaletime_limit = models.IntegerField()
	scaletime_limitstart = models.IntegerField()
	timeunit_default = models.IntegerField()
	scaleinfo_text = models.CharField(max_length=300, null = True, blank = True)
	display_symptom = models.BooleanField()
	kiosk_name = models.CharField(max_length=300, null = True, blank = True)
	formal_name = models.CharField(max_length=300, null = True, blank = True)
	definition = models.CharField(max_length=300, null = True, blank = True)
	med_necessary = models.BooleanField()
	displaydr_app = models.BooleanField()
	active = models.BooleanField()
	gender_group = models.CharField(max_length=300, null = True, blank = True)
	cardinality = models.BooleanField()
	antithesis = models.FloatField()
	snomed = models.ForeignKey(SnomedCode, on_delete=models.CASCADE)
	logical = models.ForeignKey(LogicalSymptopGroup, on_delete=models.CASCADE)
class SymptomCategory(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=300, null = True, blank = True)
	parent = models.CharField(max_length=300, null = True, blank = True)
	code = models.CharField(max_length=300, null = True, blank = True)
	bodypart_code = models.CharField(max_length=300, null = True, blank = True)
	es_name = models.CharField(max_length=300, null = True, blank = True)
	cascade_up = models.BooleanField()
	cascade_down = models.BooleanField()
	symptom_template = models.ForeignKey(SymptomTemplate, on_delete=models.CASCADE)

class SymptomGroup(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=300, null = True, blank = True)
	symptom_count = models.BooleanField()
	code = models.CharField(max_length=300, null = True, blank = True)
	group_id = models.CharField(max_length=300, null = True, blank = True)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True)
	category = models.ForeignKey(SymptomCategory, on_delete=models.CASCADE)
	def __str__(self):
		return self.id
class Symptom(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	multiple_values = models.CharField(max_length=300, null = True, blank = True)
	criticality = models.IntegerField()
	treatable = models.BooleanField()
	prior = models.DecimalField(max_digits=5, decimal_places=2)
	question = models.CharField(max_length=300, null = True, blank = True)
	es_question = models.CharField(max_length=300, null = True, blank = True)
	antithesis = models.FloatField()
	sub_groups = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	bodyparts = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	pain_swelling_id = models.IntegerField()
	display_order = models.IntegerField(default=0)
	icd_r_odes = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	display_ymptom = models.BooleanField()
	kiosk_name = models.CharField(max_length=300, null = True, blank = True)
	formal_name = models.CharField(max_length=300, null = True, blank = True)
	med_necessary = models.BooleanField()
	min_diag_criteria = models.BooleanField()
	display_dr_app = models.BooleanField()
	gender_group = models.CharField(max_length=300, null = True, blank = True)
	cardinality = models.BooleanField()
	logical_group_names = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	de_groups = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	symptom_type = models.CharField(max_length=300, null = True, blank = True)
	time_type = models.TimeField(auto_now=False, auto_now_add=False)
	min_range = models.FloatField()
	max_range = models.FloatField()
	is_range = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True)