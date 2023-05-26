from django.db import models


class Publisher(models.Model):
	name = models.CharField(max_length=30)
	genre = models.CharField(max_length=30)	
	city = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	is_active = models.BooleanField()
