from django.shortcuts import render
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('resorts/index.html', {})


def login(request):
    return render_to_response('resorts/login.html', {})