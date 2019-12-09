from django.db import models

# Create your models here.

# Create your models here.
class Student(models.Model):

	student_name 			= models.CharField(max_length=50, null=False, blank=True)
	department              = models.CharField(max_length=50, null=False, blank=True)
	contact          		= models.CharField(max_length=25, null=False, blank=True)
	
	
	def __str__(self):
		return self.student_name