from django.db import models
import datetime
import uuid
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class SymptomsTmpl(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	bias = models.BooleanField()
	rangeValues = ArrayField(
		models.DecimalField(max_digits=5, decimal_places=2),
		)
	descriptors = models.CharField(max_length=300, null = True, blank = True)
	descriptorFile = models.CharField(max_length=300, null = True, blank = True)
	questionText = models.CharField(max_length=300, null = True, blank = True)
	scaleInfoText = models.CharField(max_length=300, null = True, blank = True)
	scaleTimeLimit = models.IntegerField()
	scaleTimeLimitStart = models.IntegerField()
	timeUnitDefault = models.IntegerField()
	dataStoreTypes = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	criticality = models.IntegerField()
	treatable = models.BooleanField()
	prior = models.FloatField()
	question = models.CharField(max_length=300, null = True, blank = True)
	es_question = models.CharField(max_length=300, null = True, blank = True)
	antithesis = models.FloatField()
	displaySymptom = models.BooleanField()
	medNecessary = models.BooleanField()
	minDiagCriteria = models.BooleanField()
	displayDrApp = models.BooleanField()
	genderGroup = models.CharField(max_length=300, null = True, blank = True)
	timeType = models.TimeField(auto_now=False, auto_now_add=False)
	minRange = models.FloatField()
	maxRange = models.FloatField()
	def __str__(self):
		return self.id

class Symptoms(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	multipleValues = models.CharField(max_length=300, null = True, blank = True)
	criticality = models.IntegerField()
	treatable = models.BooleanField()
	prior = models.DecimalField(max_digits=5, decimal_places=2)
	question = models.CharField(max_length=300, null = True, blank = True)
	es_question = models.CharField(max_length=300, null = True, blank = True)
	antithesis = models.FloatField()
	subGroups = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	bodyParts = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	painSwellingID = models.IntegerField()
	displayOrder = models.IntegerField(default=0)
	icdRCodes = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	displaySymptom = models.BooleanField()
	kioskName = models.CharField(max_length=300, null = True, blank = True)
	formalName = models.CharField(max_length=300, null = True, blank = True)
	medNecessary = models.BooleanField()
	minDiagCriteria = models.BooleanField()
	displayDrApp = models.BooleanField()
	genderGroup = models.CharField(max_length=300, null = True, blank = True)
	cardinality = models.BooleanField()
	logicalGroupNames = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	deGroups = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	symptomType = models.CharField(max_length=300, null = True, blank = True)
	timeType = models.TimeField(auto_now=False, auto_now_add=False)
	minRange = models.FloatField()
	maxRange = models.FloatField()
	isRange = models.BooleanField()
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
	displayOrder = models.IntegerField()
	def __str__(self):
		return self.id
class DataKeyStore(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=300, null = True, blank = True)
	es_title = models.CharField(max_length=300, null = True, blank = True)
	values = models.ForeignKey(ValueStore, on_delete=models.CASCADE)
class SymptomGroups(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	section = models.ForeignKey(Section, on_delete=models.CASCADE)
	dataStoreRefTypes = models.ForeignKey(DataKeyStore, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.id