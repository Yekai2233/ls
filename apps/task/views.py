from django.shortcuts import render, redirect
from django.views.generic import View
from task.models import Task

# Create your views here.

class MakeTaskView(View):

	def get(self, request):
		return redirect('index')

	def post(self, request):
		try:
			task = Task()

			return redirect('index')

		except Exception as e:
			print(1111)



class ListTaskView(View):
	def get(self, request):
		task_list = Task.objects.all()
		return render(request, "task.html",
                {'task_list': task_list})