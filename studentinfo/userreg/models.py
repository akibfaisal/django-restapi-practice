from django.db import models

# Create your models here.
class User(models.Model):

	user_name 		   = models.CharField(max_length=50, null=False, blank=True)
	email              = models.CharField(max_length=50, null=False, blank=True)
	phone              = models.CharField(max_length=25, null=False, blank=True)
	password           = models.CharField(max_length=25, null=False, blank=True)
	
	def __str__(self):
		return self.user_name