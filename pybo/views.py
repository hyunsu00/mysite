from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    msg = "안녕하세요 pybo에 오신것을 환영합니다."
    return HttpResponse(msg)
