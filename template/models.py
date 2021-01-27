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

	# symptom_template = ArrayField(
	# 	models.IntegerField(blank=True, null=True)
	# 	)
	# symptom_template = models.ForeignKey(SymptomTemplate, on_delete=models.CASCADE)



class DataStoreSources(models.Model):
	source_ref_date = models.BigIntegerField(null = True, blank = True)
	source_id = models.IntegerField(null = True, blank = True)
	added_by = models.CharField(max_length=300, null = True, blank = True)
	source_info = models.CharField(max_length=300, null = True, blank = True)
	verified = models.BooleanField(null = True, blank = True)
class Scale(models.Model):
	time_frame = models.CharField(max_length=300, null = True, blank = True)
class ModifierType(models.Model):
	likelihood = models.IntegerField(default=0)
	modifier_value = models.CharField(max_length=300, null = True, blank = True)
	scale = models.ForeignKey(Scale, on_delete=models.CASCADE)
class SymptomDataStore(models.Model):
	bias = models.BooleanField(null = True, blank = True)
	multiplier = ArrayField(
		models.CharField(max_length=300, null = True, blank = True)
		)
	multiplier_code = models.CharField(max_length=300, null = True, blank = True)
	likelihood = models.IntegerField(null = True, blank = True)
	modifier_values = models.ManyToManyField(ModifierType, related_name='symptomdatastore_modifiertype', blank=True)
	likely_diseases = models.CharField(max_length=300, null = True, blank = True)
	rule_out = models.BooleanField(null = True, blank = True)
	must = models.BooleanField(null = True, blank = True)
	min_diag_criteria = models.BooleanField(null = True, blank = True)
	med_necessary = models.BooleanField(null = True, blank = True)
	source_info = models.ManyToManyField(DataStoreSources, related_name='symptomdatastore_datastoresources', blank=True)
class SymptomTmpl(models.Model):
	symptom_id = models.CharField(max_length=300, null = True, blank = True)
	bias = models.BooleanField(null=True)
	range_values = models.FloatField(null=True, blank= True)
	descriptors = models.CharField(max_length=300, null = True, blank = True)
	descriptor_file = models.CharField(max_length=300, null = True, blank = True) 
	question_text = models.CharField(max_length=300, null = True, blank = True)
	scaletime_limit = models.IntegerField(null=True, blank= True)
	scaletime_limit_start = models.IntegerField(null=True, blank= True)
	timeunit_default = models.IntegerField(null=True, blank= True)
	scaleinfo_text = models.CharField(max_length=300, null = True, blank = True)
	datastore_types = ArrayField(
		models.CharField(max_length=300, null = True, blank = True), null=True, blank=True,
		)
	criticality = models.IntegerField(blank=True, null=True)
	treatable = models.BooleanField(null=True)
	prior = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	es_question = models.CharField(max_length=300, null = True, blank = True)
	antithesis = models.FloatField(blank=True, null=True)
	display_symptom = models.BooleanField(null=True)
	med_necessary = models.BooleanField(null=True)
	min_diag_criteria = models.BooleanField(null=True)
	display_dr_app = models.BooleanField(null=True)
	gender_group = models.CharField(max_length=300, null = True, blank = True)
	time_type = models.CharField(max_length=300, null = True, blank = True)
class Symptom(models.Model):
	symtom_id = models.CharField(max_length=300, null = True, blank = True)
	multiple_values = models.CharField(max_length=300, null = True, blank = True)
	criticality = models.IntegerField(blank=True, null=True)
	treatable = models.BooleanField(null=True)
	prior = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	question = models.CharField(max_length=300, null = True, blank = True)
	es_question = models.CharField(max_length=300, null = True, blank = True)
	antithesis = models.FloatField(blank=True, null=True)
	sub_groups = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	symptoms_model = models.ForeignKey(SymptomTmpl, on_delete=models.CASCADE, null=True, blank=True)
	rows = models.ManyToManyField(SymptomDataStore, related_name='symptom_symptomdatastore', blank=True)
	pain_swelling_id = models.IntegerField(blank=True, null=True)
	display_order = models.IntegerField(default=0, null=True, blank=True)
	# icd_r_odes = ArrayField(
	# 	models.CharField(max_length=300, null = True, blank = True),
	# 	)
	display_symptom = models.BooleanField(null=True)
	# kiosk_name = models.CharField(max_length=300, null = True, blank = True)
	# formal_name = models.CharField(max_length=300, null = True, blank = True)
	# med_necessary = models.BooleanField(null=True)
	# min_diag_criteria = models.BooleanField(null=True)
	display_dr_app = models.BooleanField(null=True)
	gender_group = models.CharField(max_length=300, null = True, blank = True)
	cardinality = models.BooleanField(null=True)
	logical_group_names = ArrayField(
		models.CharField(max_length=300, null = True, blank = True), null = True, blank = True,
		)
	de_groups = ArrayField(
		models.CharField(max_length=300, null = True, blank = True), null = True, blank = True
		)
	symptom_type = models.CharField(max_length=300, null = True, blank = True)
	time_type = models.CharField(max_length=300, null = True, blank = True)
	icdrcode = models.CharField(max_length=300, null = True, blank = True)
	bias = models.BooleanField(null=True)
	active = models.BooleanField(null=True)
	time_range_start = models.IntegerField(blank=True, null=True)
	time_range_stop = models.IntegerField(blank=True, null=True)
	datastore_templates = ArrayField(
		models.CharField(max_length=300, null=True, blank=True), null=True, blank=True,
		)
	create_date = models.BigIntegerField(null=True, blank=True)
	update_date = models.BigIntegerField(null=True, blank=True)	
	# created_at = models.DateTimeField(auto_now_add=True, editable=False)
	# updated_at = models.DateTimeField(auto_now=True)

# class Category(models.Model):
# 	name = models.CharField(max_length=300, null = True, blank = True)
# 	es_name = models.CharField(max_length=300, null = True, blank = True)
# 	category_id = models.CharField(max_length=300, null = True, blank = True)
# 	symptoms = models.ManyToManyField(Symptom, related_name='category_symptom', null=True, blank=True)

class SymptomCategory(models.Model):
	name = models.CharField(max_length=300, null = True, blank = True)
	parent = models.CharField(max_length=300, null = True, blank = True)
	category_id = models.CharField(max_length=300, null = True, blank = True)
	bodypart_code = models.CharField(max_length=300, null = True, blank = True)
	es_name = models.CharField(max_length=300, null = True, blank = True)
	cascade_up = models.BooleanField(null=True)
	cascade_down = models.BooleanField(null=True)
	symptoms = models.ManyToManyField(Symptom, related_name='symptomcategory_symptom', blank=True)

class ValueStore(models.Model):
	default_value = models.BooleanField(null = True, blank = True)
	value = models.CharField(max_length=300, null = True, blank = True)
	m_antithesis = models.FloatField(null=True, blank=True)
	m_icd10_rcode = models.CharField(max_length=300, null = True, blank = True)
	count = models.IntegerField(null=True, blank=True)
	display_list_value = models.BooleanField(null = True, blank = True)
	kiosk_name = models.CharField(max_length=300, null = True, blank = True)
	es_kiosk_name = models.CharField(max_length=300, null = True, blank = True)
	display_order = models.IntegerField(null=True, blank=True)

class DataKeyStore(models.Model):
	title = models.CharField(max_length=300, null = True, blank = True)
	es_title = models.CharField(max_length=300, null = True, blank = True)
	values = models.ManyToManyField(ValueStore, related_name='datakeystore_valuestore', blank=True)
class Section(models.Model):
	name = models.CharField(max_length=300, null = True, blank = True)
	section_id = models.CharField(max_length=300, null = True, blank = True)
	categories = models.ManyToManyField(SymptomCategory, related_name='datakeystore_valuestore', blank=True)
class SymptomGroup(models.Model):
	name = models.CharField(max_length=300, null = True, blank = True)
	group_id = models.CharField(max_length=300, null = True, blank = True)
	code = models.CharField(max_length=300, null = True, blank = True)
	symptom_count = models.BooleanField(null=True, blank=True)
	sections = models.ManyToManyField(Section, related_name='symptomgroup_section', blank=True)
	categories = models.ManyToManyField(SymptomCategory, related_name='symptomgroup_category', blank=True)
	datastore_ref_types = models.ManyToManyField(DataKeyStore, related_name='symptomgroup_datakeystore', blank=True)
	create_date = models.BigIntegerField(null = True, blank = True)
	updated_date = models.BigIntegerField(null = True, blank = True)
	# created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
	# updated_at = models.DateTimeField(auto_now=True, null=True)
	# categories = models.ForeignKey(SymptomCategory, on_delete=models.CASCADE)
	# categories = models.ManyToManyField(Category, related_name='symptomgroup_category')