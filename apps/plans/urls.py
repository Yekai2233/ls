from django.urls import re_path
from plans.views import PostDetailView

app_name = 'plans'

urlpatterns = [
    re_path('process/(?P<pk>[0-9]+)/', PostDetailView.as_view(), name='plan_process'),
]
