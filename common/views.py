from django.shortcuts import render

# 여기에서보기를 만드십시오.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


# signup 함수는 POST 요청인 경우 화면에서 입력한 데이터로 새로운 사용자를 생성하고,
# GET 요청인 경우 common/signup.html 화면을 반환한다.
# POST 요청에서 form.cleaned_data.get 함수는 회원가입 화면에서 입력한 값을 얻기 위해 사용하는 함수이다.
# 여기서는 로그인 시 필요한 아이디, 비밀번호를 얻기 위해 사용되었다.
# 그리고 회원가입이 완료된 이후에 자동으로 로그인되도록 authenticate 함수와 login 함수를 사용했다.
def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
