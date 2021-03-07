# urls.py
from django.urls import path  # django.urls 패키지에서 path 모듈 가져옴

from . import views  # 현재 패키지에서 views 모듈 가져옴

app_name = 'pybo' # 네임스페이스 정의

urlpatterns = [
    path('', views.index, name = 'index'), # == path('', views.IndexView.as_view()),
    path('<int:question_id>/', views.detail, name = 'detail'), # == path('<int:pk>/', views.DetailView.as_view()),
]
    
    
