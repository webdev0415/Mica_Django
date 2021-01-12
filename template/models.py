from django.db import models
import datetime
import uuid
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class SymptomsTmpl(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	bias = models.BooleanField()
	range_values = ArrayField(
		models.DecimalField(max_digits=5, decimal_places=2),
		)
	descriptors = models.CharField(max_length=300, null = True, blank = True)
	descriptor_file = models.CharField(max_length=300, null = True, blank = True)
	question_text = models.CharField(max_length=300, null = True, blank = True)
	scale_info_text = models.CharField(max_length=300, null = True, blank = True)
	scale_time_limit = models.IntegerField()
	scale_time_limit_start = models.IntegerField()
	time_unit_default = models.IntegerField()
	datastore_types = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	criticality = models.IntegerField()
	treatable = models.BooleanField()
	prior = models.FloatField()
	question = models.CharField(max_length=300, null = True, blank = True)
	es_question = models.CharField(max_length=300, null = True, blank = True)
	antithesis = models.FloatField()
	display_symptom = models.BooleanField()
	med_necessary = models.BooleanField()
	min_diag_criteria = models.BooleanField()
	display_dr_app = models.BooleanField()
	gender_group = models.CharField(max_length=300, null = True, blank = True)
	time_type = models.TimeField(auto_now=False, auto_now_add=False)
	min_range = models.FloatField()
	max_range = models.FloatField()
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
class Category(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	category_name = models.CharField(max_length=300, null = True, blank = True)
	symptoms = models.ForeignKey(Symptoms, on_delete=models.CASCADE)
	def __str__(self):
		return self.id
class Section(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	section_name = models.CharField(max_length=300, null = True, blank = True)
	categories = models.ForeignKey(Category, on_delete=models.CASCADE)
	def __str__(self):
		return self.id
class ValueStore(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	m_antithesis = models.FloatField()
	m_icd10Rcode = models.CharField(max_length=300, null = True, blank = True)
	count = models.IntegerField()
	displayListValue = models.BooleanField()
	kiosk_name = models.CharField(max_length=300, null = True, blank = True)
	es_kiosk_name = models.CharField(max_length=300, null = True, blank = True)
	display_order = models.IntegerField()
	def __str__(self):
		return self.id
class DataKeyStore(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=300, null = True, blank = True)
	es_title = models.CharField(max_length=300, null = True, blank = True)
	values = models.ForeignKey(ValueStore, on_delete=models.CASCADE)
class SymptomGroup(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	section = models.ForeignKey(Section, on_delete=models.CASCADE)
	datastore_ref_types = models.ForeignKey(DataKeyStore, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.id