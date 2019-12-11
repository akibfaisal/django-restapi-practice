from django.db import models

# Create your models here.
class Info(models.Model):

	reg_number 		= models.CharField(max_length=50, null=False, blank=False)
	ein1            = models.CharField(max_length=50, null=False, blank=True)
	ein2          	= models.CharField(max_length=50, null=False, blank=True)
	ein3 			= models.CharField(max_length=50, null=False, blank=True)
	nid             = models.CharField(max_length=50, null=False, blank=True)
	amount          = models.CharField(max_length=50, null=False, blank=True)
	
	def __str__(self):
		return self.reg_number