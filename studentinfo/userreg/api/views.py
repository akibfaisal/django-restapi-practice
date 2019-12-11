from userreg.models import User
from rest_framework.generics import ListAPIView
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from userreg.api.serializers import  UserSerializer,UserCreateSerializer,UserUpdateSerializer
# Create your views here.
##############################
SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

@api_view(['DELETE',])
#@permission_classes((IsAuthenticated, ))
def api_delete_userreg_view(request, pk):

	try:
		user_reg = User.objects.get(pk=pk)
	except User.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)


	if request.method == 'DELETE':
		operation = user_reg.delete()
		data = {}
		if operation:
			data['response'] = DELETE_SUCCESS
		return Response(data=data)

@api_view(['PUT'])
def api_update_userreg_view(request,pk):

	try:
		user_reg = User.objects.get(pk=pk)
		#print (info_user.image_file)
	except User.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'PUT':
		serializer = UserUpdateSerializer(user_reg, data=request.data, partial=True)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data['response'] = UPDATE_SUCCESS
			data['pk'] = user_reg.pk
			data['user_name'] = user_reg.user_name
			data['email'] = user_reg.email
			data['phone'] = user_reg.phone
			data['password'] = user_reg.password
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api_create_userreg_view(request):

	if request.method == 'POST':
		print("inside create method!!!!!")
		data = request.data
		serializerboard = UserCreateSerializer(data=data)

		data = {}
		if serializerboard.is_valid():
			info = serializerboard.save()
			data['response'] = CREATE_SUCCESS
			data['pk'] = info.pk
			data['user_name'] = info.user_name
			data['email'] = info.email
			data['phone'] = info.phone
			data['password'] = info.password
			# data['contact_number'] = info.contact_number
			# data['email']  = info.email
			# data['group_number'] = info.group_number
			return Response(data=data)
		return Response(serializerboard.errors, status=status.HTTP_400_BAD_REQUEST)

class  UserListView(ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	pagination_class = PageNumberPagination
	filter_backends = (SearchFilter, OrderingFilter)
	search_fields = ('user_name', 'phone')
