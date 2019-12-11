from django.urls import path,include
from collegeapp.api import views
from collegeapp.api.views import(
      api_create_collegeapp_view,
      api_update_collegeapp_view,
      api_delete_collegeapp_view,
      InfoListView
)

app_name = 'collegeapp'

urlpatterns = [
   
    path('list', InfoListView.as_view(), name="list"),
	path('create', api_create_collegeapp_view, name="create"),
	path('update/<pk>', api_update_collegeapp_view, name="update"),
	path('delete/<pk>',api_delete_collegeapp_view, name ="delete")

]