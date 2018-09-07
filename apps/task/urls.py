from django.urls import re_path
from task.views import MakeTaskView

app_name = 'task'

urlpatterns = [
	re_path(r'^send_parameter/', MakeTaskView.as_view(), name='send_parameter')
]

