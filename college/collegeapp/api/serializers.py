from rest_framework import serializers
from collegeapp.models import Info
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
#from books.models import Book
#from books.apibooks.serializers import BookSerializer

class InfoUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Info
		fields = ('pk','reg_number', 'ein1', 'ein2', 'ein3', 'nid', 'amount')

class InfoSerializer(serializers.ModelSerializer):
	#personalinfo = BookSerializer(many=True)
	class Meta:
		model = Info
		fields = ('pk','reg_number', 'ein1', 'ein2', 'ein3', 'nid', 'amount')

class  InfoCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Info
		fields = ('reg_number', 'ein1', 'ein2', 'ein3', 'nid', 'amount')

	def save(self):
		try:
			reg_number      = self.validated_data['reg_number']
			ein1        	= self.validated_data['ein1']
			ein2            = self.validated_data['ein2']
			ein3            = self.validated_data['ein3']
			nid             = self.validated_data['nid']
			amount          = self.validated_data['amount']
	
			collegeapp = Info(
								reg_number=reg_number,
								ein1=ein1,
								ein2=ein2,
								ein3=ein3,
								nid=nid,
								amount=amount
								)
			collegeapp.save()
			return collegeapp
		except KeyError:
			raise serializers.ValidationError({"response": "this invalid somethings!!!!!"})