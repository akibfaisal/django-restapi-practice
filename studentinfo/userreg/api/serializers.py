from rest_framework import serializers
from userreg.models import User
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

#from books.models import Book
#from books.apibooks.serializers import BookSerializer

class UserUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('pk','user_name', 'email', 'phone', 'password')

class UserSerializer(serializers.ModelSerializer):
	#personalinfo = BookSerializer(many=True)
	class Meta:
		model = User
		fields = ('pk','user_name', 'email', 'phone', 'password')

class  UserCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('user_name', 'email', 'phone', 'password')

	def save(self):
		try:
			user_name    = self.validated_data['user_name']
			email        = self.validated_data['email']
			phone        = self.validated_data['phone']
			password     = self.validated_data['password']
	
			reginfo = User(
							user_name=user_name,
							email=email,
							phone=phone,
							password=password
							)
			reginfo.save()
			return reginfo
		except KeyError:
			raise serializers.ValidationError({"response": "this invalid somethings!!!!!"})