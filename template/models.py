from django.db import models
import datetime
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class SnomedCode(models.Model):
	code = models.CharField(max_length=300, null = True, blank = True)
	name = models.CharField(max_length=300, null = True, blank = True)
	concept_id = ArrayField(
		models.BigIntegerField(blank=True, null=True),
		)
	expression = models.CharField(max_length=300, null = True, blank = True)
	list_valuecode = models.CharField(max_length=300, null = True, blank = True)
	type = models.CharField(max_length=300, null = True, blank = True)
	def __str__(self):
		return self.name
class LogicalSymptopGroup(models.Model):
	group_id = models.IntegerField(blank=True, null=True)
	group_flag = models.CharField(max_length=300, null = True, blank = True)
class RcodeDatastore(models.Model):
	m_icd10_rcode = models.CharField(max_length=300, null = True, blank = True)
	ds_code = models.CharField(max_length=300, null = True, blank = True)
	code = models.CharField(max_length=300, null = True, blank = True)
class SymptomTemplate(models.Model):
	criticality = models.IntegerField(blank=True, null=True)
	treatable = models.BooleanField(null=True)
	multiple_values = models.CharField(max_length=300, null = True, blank = True)
	code = models.CharField(max_length=300, null = True, blank = True)
	time_type = models.CharField(max_length=300, null = True, blank = True)
	question_text = models.CharField(max_length=300, null = True, blank = True)
	icdrcode = models.CharField(max_length=300, null = True, blank = True)
	es_question = models.CharField(max_length=300, null = True, blank = True)
	es_question_bk = models.CharField(max_length=300, null = True, blank = True)
	name = models.CharField(max_length=300, null = True, blank = True)
	es_name = models.CharField(max_length=300, null = True, blank = True)
	symptom_type = models.CharField(max_length=300, null = True, blank = True)
	px_no_normalized = models.FloatField(blank=True, null=True)
	prior = models.FloatField(blank=True, null=True)
	definition = models.CharField(max_length=300, null = True, blank = True)
	painswelling_id = models.IntegerField(blank=True, null=True)
	display_order = models.IntegerField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)
	bias = models.BooleanField(null=True)
	descriptor_file = models.CharField(max_length=300, null = True, blank = True)
	scaletime_limit_text = models.CharField(max_length=300, null = True, blank = True)
	timeunit_default = models.IntegerField(blank=True, null=True)
	display_symptom = models.BooleanField(null=True)
	displaydr_app = models.BooleanField(null=True)
	active = models.BooleanField(null=True)
	gender_group = models.CharField(max_length=300, null = True, blank = True)
	cardinality = models.BooleanField(null=True)
	antithesis = models.FloatField(blank=True, null=True)
	time_range_start = models.IntegerField(blank=True, null=True)
	time_range_stop = models.IntegerField(blank=True, null=True)
	sub_groups = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	datastore_templates = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	# snomed = models.ForeignKey(SnomedCode, on_delete=models.CASCADE)
	# logical = models.ForeignKey(LogicalSymptopGroup, on_delete=models.CASCADE)
	snomed = ArrayField(
		models.IntegerField(blank=True, null=True)
		)
	logical = ArrayField(
		models.IntegerField(blank=True, null=True)
		)
	rcode = ArrayField(
		models.IntegerField(blank=True, null=True)
		)
class SymptomCategory(models.Model):
	name = models.CharField(max_length=300, null = True, blank = True)
	parent = models.CharField(max_length=300, null = True, blank = True)
	code = models.CharField(max_length=300, null = True, blank = True)
	bodypart_code = models.CharField(max_length=300, null = True, blank = True)
	es_name = models.CharField(max_length=300, null = True, blank = True)
	cascade_up = models.BooleanField(null=True)
	cascade_down = models.BooleanField(null=True)
	symptom_template = ArrayField(
		models.IntegerField(blank=True, null=True)
		)
	# symptom_template = models.ForeignKey(SymptomTemplate, on_delete=models.CASCADE)

class SymptomGroup(models.Model):
	name = models.CharField(max_length=300, null = True, blank = True)
	symptom_count = models.BooleanField(null=True)
	code = models.CharField(max_length=300, null = True, blank = True)
	group_id = models.CharField(max_length=300, null = True, blank = True)
	created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)
	# category = models.ForeignKey(SymptomCategory, on_delete=models.CASCADE)
	category = ArrayField(
		models.IntegerField(blank=True, null=True)
		)
	def __str__(self):
		return self.id
class Symptom(models.Model):
	multiple_values = models.CharField(max_length=300, null = True, blank = True)
	criticality = models.IntegerField(blank=True, null=True)
	treatable = models.BooleanField(null=True)
	prior = models.DecimalField(max_digits=5, decimal_places=2)
	question = models.CharField(max_length=300, null = True, blank = True)
	es_question = models.CharField(max_length=300, null = True, blank = True)
	antithesis = models.FloatField(blank=True, null=True)
	sub_groups = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	bodyparts = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	pain_swelling_id = models.IntegerField(blank=True, null=True)
	display_order = models.IntegerField(default=0)
	icd_r_odes = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	display_ymptom = models.BooleanField(null=True)
	kiosk_name = models.CharField(max_length=300, null = True, blank = True)
	formal_name = models.CharField(max_length=300, null = True, blank = True)
	med_necessary = models.BooleanField(null=True)
	min_diag_criteria = models.BooleanField(null=True)
	display_dr_app = models.BooleanField(null=True)
	gender_group = models.CharField(max_length=300, null = True, blank = True)
	cardinality = models.BooleanField(null=True)
	logical_group_names = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	de_groups = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	symptom_type = models.CharField(max_length=300, null = True, blank = True)
	time_type = models.TimeField(auto_now=False, auto_now_add=False)
	min_range = models.FloatField(blank=True, null=True)
	max_range = models.FloatField(blank=True, null=True)
	is_range = models.BooleanField(null=True)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True)