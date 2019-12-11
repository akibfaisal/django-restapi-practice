from django.urls import path,include
from userreg.api import views
from userreg.api.views import(
      api_create_userreg_view,
      api_update_userreg_view,
      api_delete_userreg_view,
      UserListView
)

app_name = 'userreg'

urlpatterns = [
   
    path('list', UserListView.as_view(), name="list"),
	path('create', api_create_userreg_view, name="create"),
	path('update/<pk>', api_update_userreg_view, name="update"),
	path('delete/<pk>',api_delete_userreg_view, name ="delete")

]