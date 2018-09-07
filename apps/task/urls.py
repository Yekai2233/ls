from django.urls import re_path
from task.views import MakeTaskView, ListTaskView

app_name = 'task'

urlpatterns = [
	re_path(r'^send_parameter/', MakeTaskView.as_view(), name='send_parameter'),
	re_path(r'^list_task/', ListTaskView.as_view(), name='list_task')
]

