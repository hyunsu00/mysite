# answer_views.py
# 답변관리

# 메시지 출력
from django.contrib import messages

# 로그인이 필요한 함수에 @login_required 애너테이션 적용하기
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import AnswerForm
from ..models import Question, Answer

# AnonymousUser로 인한 오류 @login_required 애너테이션을 사용하여 수정
@login_required(login_url="common:login")
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # 추가한 속성 author 적용
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            # return redirect("pybo:detail", question_id=question.id)

            # pybo:detail에 #answer_2와 같은 앵커를 추가하기 위해 format과 resolve_url 함수를 사용했다.
            # resolve_url 함수는 실제 호출되는 URL을 문자열로 반환하는 장고 함수이다.
            # <a name="answer_{{ answer.id }}"></a> 위치로 스크롤됨
            to = "{}#answer_{}".format(resolve_url("pybo:detail", question_id=question.id), answer.id)
            return redirect(to)
    else:
        form = AnswerForm()
    context = {"question": question, "form": form}
    return render(request, "pybo/question_detail.html", context)


@login_required(login_url="common:login")
def answer_modify(request, answer_id):
    """
    pybo 답변수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, "수정권한이 없습니다")
        return redirect("pybo:detail", question_id=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            # return redirect("pybo:detail", question_id=answer.question.id)

            # pybo:detail에 #answer_2와 같은 앵커를 추가하기 위해 format과 resolve_url 함수를 사용했다.
            # resolve_url 함수는 실제 호출되는 URL을 문자열로 반환하는 장고 함수이다.
            # <a name="answer_{{ answer.id }}"></a> 위치로 스크롤됨
            to = "{}#answer_{}".format(resolve_url("pybo:detail", question_id=answer.question.id), answer.id)
            return redirect(to)
    else:
        form = AnswerForm(instance=answer)
    context = {"answer": answer, "form": form}
    return render(request, "pybo/answer_form.html", context)


@login_required(login_url="common:login")
def answer_delete(request, answer_id):
    """
    pybo 답변삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, "삭제권한이 없습니다")
    else:
        answer.delete()
    return redirect("pybo:detail", question_id=answer.question.id)