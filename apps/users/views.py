from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render
# Create your views here.


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')
