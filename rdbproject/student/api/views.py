from student.models import Student
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
from student.api.serializers import  StudentSerializer,StudentCreateSerializer,StudentUpdateSerializer
# Create your views here.
##############################
SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

@api_view(['DELETE',])
#@permission_classes((IsAuthenticated, ))
def api_delete_student_view(request, pk):

	try:
		info_user = Student.objects.get(pk=pk)
	except Student.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)


	if request.method == 'DELETE':
		operation = info_user.delete()
		data = {}
		if operation:
			data['response'] = DELETE_SUCCESS
		return Response(data=data)

@api_view(['PUT'])
def api_update_student_view(request,pk):

	try:
		info_user = Student.objects.get(pk=pk)
		#print (info_user.image_file)
	except Student.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'PUT':
		serializer = StudentUpdateSerializer(info_user, data=request.data, partial=True)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data['response'] = UPDATE_SUCCESS
			data['pk'] = info_user.pk
			data['student_name'] = info_user.student_name
			data['department'] = info_user.department
			data['contact'] = info_user.contact
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api_create_student_view(request):

	if request.method == 'POST':
		print("inside create method!!!!!")
		data = request.data
		serializerboard = StudentCreateSerializer(data=data)

		data = {}
		if serializerboard.is_valid():
			info = serializerboard.save()
			data['response'] = CREATE_SUCCESS
			data['pk'] = info.pk
			data['student_name'] = info.student_name
			data['department'] = info.department
			data['contact'] = info.contact
			# data['gender']   = info.gender
			# data['contact_number'] = info.contact_number
			# data['email']  = info.email
			# data['group_number'] = info.group_number
			return Response(data=data)
		return Response(serializerboard.errors, status=status.HTTP_400_BAD_REQUEST)

class  StudentListView(ListAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	pagination_class = PageNumberPagination
	filter_backends = (SearchFilter, OrderingFilter)
	search_fields = ('student_name', 'contact')
