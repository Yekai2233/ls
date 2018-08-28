from django.urls import re_path, path
from plans.views import ProcessDetailView, CreatePlanView, EditPlanView, CreateProcessView

app_name = 'plans'

urlpatterns = [
    re_path(r'^plan/(?P<pk>[0-9]+)/', ProcessDetailView.as_view(), name='plan_process'),
    path(r'createplan/', CreatePlanView.as_view(), name='create_plan'),
    re_path(r'^editplan/(?P<pk>[0-9]+)\d+/', EditPlanView.as_view(), name='edit_plan'),
    re_path(r'^createprocess/(?P<pk>[0-9]+)/', CreateProcessView.as_view(), name='create_process'),
]
