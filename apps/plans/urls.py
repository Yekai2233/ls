from django.urls import re_path, path
from plans.views import ProcessListView, CreatePlanView, EditPlanView, CreateProcessView

app_name = 'plans'

urlpatterns = [
    re_path(r'^plan/(?P<plan_id>[0-9]+)/', ProcessListView.as_view(), name='process'),
    path(r'createplan/', CreatePlanView.as_view(), name='create_plan'),
    re_path(r'^editplan/(?P<plan_id>[0-9]+)\d+/', EditPlanView.as_view(), name='edit_plan'),
    re_path(r'^createprocess/(?P<pk>[0-9]+)/', CreateProcessView.as_view(), name='create_process'),
]
