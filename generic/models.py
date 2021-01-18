from django.db import models
import datetime
import uuid
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class BodyPart(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	group_name = models.CharField(max_length=300, null = True, blank = True)
	parent_id = models.IntegerField()
	bodypart_id = models.CharField(max_length=300, null = True, blank = True)
	es_name = models.CharField(max_length=300, null = True, blank = True)
	name = models.CharField(max_length=300, null = True, blank = True)
	position = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	es_position = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	bodyparts_codes = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	position = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	sub_parts = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	def __str__(self):
		return self.id
