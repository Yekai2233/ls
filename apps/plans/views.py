from django.shortcuts import render
from django.views.generic.base import View
from apps.plans.models import Process, Plans
from users.views import pag_not_found
# Create your views here.


class PostDetailView(View):
    def get(self, request, pk):
        process_list = Process.objects.filter(plan_id=int(pk))
        plan = Plans.objects.get(id=int(pk))
        if process_list:
            return render(request, "single.html",
                          {'process': process_list,
                            'plan': plan
                           })

        else:
            return pag_not_found(request)

    # def post(self, request):
