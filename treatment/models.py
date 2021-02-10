from django.db import models
import datetime
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class TreatmentTypeRefDesc(models.Model):
	concept_id = ArrayField(
		models.BigIntegerField(null = True, blank = True), null=True, blank=True
		)
	cpt_code = ArrayField(
		models.CharField(max_length=300, null = True, blank = True), null=True, blank=True
		)
	default_value = models.BooleanField(null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	short_name = models.CharField(max_length=300, null = True, blank = True)
	long_name = models.CharField(max_length=300, null = True, blank = True)
	priority = models.IntegerField(blank=True, null=True)
	typedesc_id = models.IntegerField(null=True, blank=True)
	# class Meta:
	# 	managed = False
	# created_at = models.DateTimeField(auto_now_add=True, editable=False)
	# updated_at = models.DateTimeField(auto_now=True)
	# def __str__(self):
	# 	return self.id

class TreatmentTypeRefModel(models.Model):
	# code = models.CharField(max_length=300, null = True, blank = True)
	name = models.CharField(max_length=300, null = True, blank = True)
	# es_name = models.CharField(max_length=300, null = True, blank = True)
	treatment_type_desc = models.ManyToManyField(TreatmentTypeRefDesc, related_name='treatmenttype_treatmenttypedesc', blank=True)
	tre_type = models.CharField(max_length=300, null = True, blank = True)
	type_id = models.IntegerField(blank=True, null=True)
	active = models.BooleanField(blank=True, null=True)
	# created_at = models.DateTimeField(auto_now_add=True, editable=False)
	# updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

# class TreatmentTypeRef(models.Model):
# 	code = models.CharField(max_length=300, null = True, blank = True)
# 	name = models.CharField(max_length=300, null = True, blank = True)
# 	es_name = models.CharField(max_length=300, null = True, blank = True)
# 	# treatment_type = models.ForeignKey(TreatmentTypeRefModel, on_delete=models.CASCADE)
# 	treatment_type_desc = models.ManyToManyField(TreatmentTypeRefDesc, related_name='treatmenttype_treatmenttypedesc', blank=True)
# 	created_at = models.DateTimeField(auto_now_add=True, editable=False)
# 	updated_at = models.DateTimeField(auto_now=True)
# 	def __str__(self):
# 		return self.name
# class Drug(models.Model):
# 	name = models.CharField(max_length=300, null = True, blank = True)
# 	rank = models.IntegerField(null = True)
# 	ingredient_rxcui = models.IntegerField(null = True)
# 	ingredient_rxcui_desc = models.CharField(max_length=300, null = True, blank = True)
# 	rxcui = models.IntegerField(null = True)
# 	added_by = models.CharField(max_length=300, null = True, blank = True)
# 	tty = models.CharField(max_length=300, null = True, blank = True)
# 	product_id = models.CharField(max_length=300, null = True, blank = True)
# 	sources = ArrayField(
# 		models.IntegerField(null = True)
# 		)
# class NonDrug(models.Model):
# 	short_name = models.CharField(max_length=300, null = True, blank = True)
# 	long_name = models.CharField(max_length=300, null = True, blank = True)
# 	priority = models.IntegerField(null = True)
# 	type_desc_id = models.IntegerField(null = True)
# 	rank = models.IntegerField(null = True)
# 	description = models.CharField(max_length=300, null = True, blank = True)
# 	notes = models.CharField(max_length=300, null = True, blank = True)
# 	sources = ArrayField(
# 		models.IntegerField(null = True)
# 		)

# class TreatmentGroup(models.Model):
# 	name = models.CharField(max_length=300, null = True, blank = True)
# 	old_name = models.CharField(max_length=300, null = True, blank = True)
# 	load = models.BooleanField(null = True)
# 	code = models.CharField(max_length=300, null = True, blank = True)
# 	rank = models.IntegerField(null = True)
# 	non_drugs = ArrayField(
# 		models.IntegerField()
# 		)
# 	non_drugs_descriptions = ArrayField(
# 		models.CharField(max_length=300, null = True, blank = True)
# 		)
# 	drugs = ArrayField(
# 		models.IntegerField( null = True)
# 		)
# 	drugs_descriptions =  ArrayField(
# 		models.CharField(max_length=300, null = True, blank = True)
# 		)
# class Treatment(models.Model):
# 	type_id = models.IntegerField(null = True)
# 	treatment_group = ArrayField(
# 		models.IntegerField(null = True)
# 		)

