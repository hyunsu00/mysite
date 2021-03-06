# urls.py
from django.urls import path  # django.urls 패키지에서 path 모듈 가져옴

from . import views  # 현재 패키지에서 views 모듈 가져옴

urlpatterns = [
    path('', views.index),
]
