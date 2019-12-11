from django.db import models
from userreg.models import User

# Create your models here.
class Details(models.Model):

	first_name 				= models.CharField(max_length=50, null=False, blank=True)
	last_name 				= models.CharField(max_length=50, null=False, blank=True)
	dept                	= models.CharField(max_length=50, null=False, blank=True)
	semester                = models.CharField(max_length=50, null=False, blank=True)
	uid               		= models.ForeignKey(User,related_name='userID', on_delete=models.CASCADE, blank=True)



	def __str__(self):
		return self.first_name

