from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View
from apps.plans.models import Process, Plans
from users.views import pag_not_found
from django.http import HttpResponse
# Create your views here.


class ProcessDetailView(View):
    def get(self, request, pk):
        process_list = Process.objects.filter(plan_id_id=int(pk))
        plan = Plans.objects.get(id=int(pk))

        if plan:
            return render(request, "single.html",
                {'process_list': process_list,
                'plan': plan,
                })
        else:
            return pag_not_found(request)


class CreateProcessView(View):
    def get(self, request, pk):
        return render(request, 'create_process.html', {'pk': pk})

    def post(self, request, pk):
        process = Process()
        process.process_name = request.POST.get('process_name')
        process.start_time = request.POST.get('start_time')
        process.end_time = request.POST.get('end_time')
        process.content = request.POST.get('content')
        process.plan_id_id = pk
        print('sssssssssssssssss')
        process.save()
        print('sss22222222222ss')
        return redirect('plans:plan_process', pk)


class CreatePlanView(View):
    def get(self, request):

        return render(request, 'create_plan.html')

    def post(self, request):

        author_id = request.user.id
        nu = Plans.objects.filter(author_id=author_id).count()
        if nu >= 4:
            return redirect('index')

        goal = request.POST.getlist('goal')
        now_status = request.POST.get('now_status')
        future_status = request.POST.get('future_status')
        plan = Plans(goal=goal, now_status=now_status, future_status=future_status, author_id=author_id)
        plan.save()

        return redirect('index')


class EditPlanView(View):
    def get(self, request, pk):
        plan = Plans.objects.get(id=int(pk))
        return render(request, 'create_plan.html', {'plan': plan})

    def post(self, request, pk):
        plan = Plans.objects.get(id=int(pk))
        plan.goal = request.POST.get('goal')
        plan.now_status = request.POST.get('now_status')
        plan.future_status = request.POST.get('future_status')
        plan.author_id = request.user.id
        print(plan.future_status)
        plan.save()
        return redirect(reverse('index'))


# class EditProcessView(View):
#     def get(self, request, pk):
#         plan = Plans.objects.get(id=int(pk))
#         print(plan.id)
#         return render(request, 'create_plan.html', {'plan': plan})
