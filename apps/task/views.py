from django.shortcuts import render, redirect
from django.views.generic import View
from task.models import Task

# Create your views here.

class MakeTaskView(View):

    def post(self, request):
        try:
            task = Task()

            return redirect('index')

        except Exception as e:

            return render