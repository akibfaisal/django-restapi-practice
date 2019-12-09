from django.urls import path,include
from student.api import views
from student.api.views import(
      api_create_student_view,
      api_update_student_view,
      api_delete_student_view,
      StudentListView
)

app_name = 'student'

urlpatterns = [
   
    path('list', StudentListView.as_view(), name="list"),
	path('create', api_create_student_view, name="create"),
	path('update/<pk>', api_update_student_view, name="update"),
	path('delete/<pk>',api_delete_student_view, name ="delete")

]