from django.db import models

# Create your models here.
class Member(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Meeting(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	date = models.DateTimeField()
	location = models.CharField(max_length=100, blank=True, null=True)
	participants = models.ManyToManyField(Member, blank=True)

	def __str__(self):
		return self.name
class MeetingItem(models.Model):
	name = models.CharField(max_length=100)
	description =  models.CharField(max_length=500)
	meeting = models.ForeignKey(Meeting)
	presenter = models.ForeignKey(Member, null=True)

	def __str__(self):
		return self.name