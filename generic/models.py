from django.db import models
import datetime
import uuid
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class BodyPart(models.Model):
	group_name = models.CharField(max_length=300, null = True, blank = True)
	bodypart_code = models.CharField(max_length=300, null = True, blank = True)
	parent_id = models.IntegerField(null = True)
	es_name = models.CharField(max_length=300, null = True, blank = True)
	name = models.CharField(max_length=300, null = True, blank = True)
	position = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	sub_parts = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)