from django.shortcuts import render

from .models import Resort
from .models import Grade


def index(request):
    latest_resort_list = Resort.objects.all()
    latest_grade_list = Grade.objects.all()
    context = {'latest_resort_list': latest_resort_list, 'latest_grade_list': latest_grade_list }
    return render(request, 'grades/index.html', context)