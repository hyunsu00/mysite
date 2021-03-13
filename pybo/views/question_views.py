# question_views.py
# 질문관리

# 메시지 출력
from django.contrib import messages

# 로그인이 필요한 함수에 @login_required 애너테이션 적용하기
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question

# URL 매핑에 의해 실행될 views.question_create 함수를 작성
# {'form': form}은 템플릿에서 폼 엘리먼트를 생성할 때 사용
# AnonymousUser로 인한 오류 @login_required 애너테이션을 사용하여 수정
@login_required(login_url="common:login")
def question_create(request):
    """
    pybo 질문등록
    """
    """
    # URL 요청을 POST, GET 요청 방식에 따라 다르게 처리한 부분이다. 
    # 질문 목록 화면에서 <질문 등록하기> 버튼을 누르면 /pybo/question/create/가 GET 방식으로 요청되어 
    # 질문 등록 화면이 나타나고, 질문 등록 화면에서 입력값을 채우고 <저장하기> 버튼을 누르면 
    # /pybo/question/create/가 POST 방식으로 요청되어 데이터가 저장된다.
    """
    """
    # QuestionForm 객체도 GET 방식과 POST 방식일 경우 다르게 생성한 것에 주목하자. 
    # GET 방식의 경우 QuestionForm()과 같이 입력값 없이 객체를 생성했고 POST 방식의 경우에는 
    # QuestionForm(request.POST)처럼 화면에서 전달받은 데이터로 폼의 값이 채워지도록 객체를 생성했다. 
    # form.is_valid 함수는 POST 요청으로 받은 form이 유효한지 검사한다. 
    # 폼이 유효하지 않다면 폼에 오류가 저장되어 화면에 전달될 것이다.
    """
    """
    # question = form.save(commit=False)는 form으로 Question 모델 데이터를 저장하기 위한 코드이다. 
    # 여기서 commit=False는 임시 저장을 의미한다.
    # 실제 데이터는 아직 저장되지 않은 상태를 말한다. 
    # 이렇게 임시 저장을 사용하는 이유는 폼으로 질문 데이터를 저장할 경우 Question 모델의 
    # create_date에 값이 설정되지 않아 오류가 발생하기 때문이다(폼에는 현재 subject, content 필드만 있고 
    # create_date 필드는 없다). 이러한 이유로 임시 저장을 한 후 question 객체를 반환받아 
    # create_date에 값을 설정한 후 question.save()로 실제 저장하는 것이다.
    """
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # 추가한 속성 author 적용
            question.create_date = timezone.now()
            question.save()
            return redirect("pybo:index")
    else:
        form = QuestionForm()

    context = {"form": form}
    return render(request, "pybo/question_form.html", context)


@login_required(login_url="common:login")
def question_modify(request, question_id):
    """
    pybo 질문수정
    """
    """
    question_modify 함수는 로그인한 사용자(request.user)와 수정하려는 글쓴이(question.author)가 다르면 '수정권한이 없습니다'라는 오류가 발생하도록 작성
    - '수정권한이 없습니다' 오류를 발생시키기 위해 messages 모듈을 이용했다.
    - messages 모듈은 장고가 제공하는 기능으로 오류를 임의로 발생시키고 싶은 경우에 사용한다. 
      이때 임의로 발생시킨 오류는 폼 필드와 관련이 없으므로 넌필드 오류에 해당된다.
    """
    """
    질문 상세 화면에서 <수정>을 누르면 /pybo/question/modify/2/ 페이지가 GET 방식으로 호출되어 질문 수정 화면이 나타나고, 
    질문 수정 화면에서 <저장하기>를 누르면 /pybo/question/modify/2/ 페이지가 POST 방식으로 호출되어 데이터 수정이 이뤄진다.
    - 데이터 저장 시 form 엘리먼트에 action 속성이 없으면 현재의 페이지로 폼을 전송한다.
    - 질문 수정에서 사용한 템플릿은 질문 등록 시 사용한 pybo/question_form.html 파일을 그대로 사용한다.
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, "수정권한이 없습니다")
        return redirect("pybo:detail", question_id=question.id)

    if request.method == "POST":
        # [질문 수정을 위해 값 덮어쓰기]
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()  # [질문 수정일시를 현재일시로 저장]
            question.save()
            return redirect("pybo:detail", question_id=question.id)
    else:
        # [질문 수정 화면에 기존 제목, 내용 반영]
        form = QuestionForm(instance=question)
    context = {"form": form}
    return render(request, "pybo/question_form.html", context)


@login_required(login_url="common:login")
def question_delete(request, question_id):
    """
    pybo 질문삭제
    """
    """
    question_delete 함수 역시 로그인이 필요하므로 @login_required 애너테이션을 적용하고 로그인한 사용자와 글쓴이가 동일한 경우에만 삭제할 수 있도록 했다.
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, "삭제권한이 없습니다")
        return redirect("pybo:detail", question_id=question.id)
    question.delete()
    return redirect("pybo:index")