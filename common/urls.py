# urls.py

from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'common'


urlpatterns = [
    # LoginView는 registration이라는 템플릿 디렉터리에서 login.html 파일을 찾는다.
    # 따라서 login.html 파일을 작성해야 한다.
    # as_view 함수에 template_name으로 'common/login.html'을 설정하면 registration 디렉터리가 아닌 common 디렉터리에서 login.html 파일을 참조하게 된다.
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup')
]
