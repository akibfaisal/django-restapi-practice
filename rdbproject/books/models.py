from django.db import models
from student.models import Student

# Create your models here.
class Book(models.Model):

	book_name 				= models.CharField(max_length=50, null=False, blank=True)
	category                = models.CharField(max_length=50, null=False, blank=True)
	#book_file               = models.FileField(null =False, blank=True),
	studentid               = models.ForeignKey(Student,related_name='studentinfo', on_delete=models.CASCADE, blank=True)



	def __str__(self):
		return self.book_name

