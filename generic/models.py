from django.db import models
import datetime
import uuid
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class BodyParts(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	groupName = models.CharField(max_length=300, null = True, blank = True)
	position = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	es_position = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	bodyPartsCodes = ArrayField(
		models.CharField(max_length=300, null = True, blank = True),
		)
	parentID = models.IntegerField()
	def __str__(self):
		return self.id
