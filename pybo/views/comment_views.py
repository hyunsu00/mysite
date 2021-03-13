# comment_views.py
# 댓글관리

# 메시지 출력
from django.contrib import messages

# 로그인이 필요한 함수에 @login_required 애너테이션 적용하기
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import CommentForm
from ..models import Question, Answer, Comment

# 질문 댓글 등록 함수 추가
@login_required(login_url="common:login")
def comment_create_question(request, question_id):
    """
    pybo 질문댓글등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            # return redirect("pybo:detail", question_id=question.id)

            # pybo:detail에 #comment_2와 같은 앵커를 추가하기 위해 format과 resolve_url 함수를 사용했다.
            # resolve_url 함수는 실제 호출되는 URL을 문자열로 반환하는 장고 함수이다.
            # <a name="comment_{{ comment.id }}"></a> 위치로 스크롤됨
            to = "{}#comment_{}".format(resolve_url("pybo:detail", question_id=comment.question.id), comment.id)
            return redirect(to)
    else:
        form = CommentForm()
    context = {"form": form}
    return render(request, "pybo/comment_form.html", context)


# 질문 댓글 수정 함수 추가
@login_required(login_url="common:login")
def comment_modify_question(request, comment_id):
    """
    pybo 질문댓글수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, "댓글수정권한이 없습니다")
        return redirect("pybo:detail", question_id=comment.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            # return redirect("pybo:detail", question_id=comment.question.id)

            # pybo:detail에 #comment_2와 같은 앵커를 추가하기 위해 format과 resolve_url 함수를 사용했다.
            # resolve_url 함수는 실제 호출되는 URL을 문자열로 반환하는 장고 함수이다.
            # <a name="comment_{{ comment.id }}"></a> 위치로 스크롤됨
            to = "{}#comment_{}".format(resolve_url("pybo:detail", question_id=comment.question.id), comment.id)
            return redirect(to)
    else:
        form = CommentForm(instance=comment)
    context = {"form": form}
    return render(request, "pybo/comment_form.html", context)


# 질문 댓글 삭제 함수 추가
@login_required(login_url="common:login")
def comment_delete_question(request, comment_id):
    """
    pybo 질문댓글삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, "댓글삭제권한이 없습니다")
        return redirect("pybo:detail", question_id=comment.question.id)
    else:
        comment.delete()
    return redirect("pybo:detail", question_id=comment.question.id)


# 답변 댓글 등록, 수정, 삭제 함수 추가하기
@login_required(login_url="common:login")
def comment_create_answer(request, answer_id):
    """
    pybo 답글댓글등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            # return redirect("pybo:detail", question_id=comment.answer.question.id)

            # pybo:detail에 #comment_2와 같은 앵커를 추가하기 위해 format과 resolve_url 함수를 사용했다.
            # resolve_url 함수는 실제 호출되는 URL을 문자열로 반환하는 장고 함수이다.
            # <a name="comment_{{ comment.id }}"></a> 위치로 스크롤됨
            to = "{}#comment_{}".format(resolve_url("pybo:detail", question_id=comment.answer.question.id), comment.id)
            return redirect(to)
    else:
        form = CommentForm()
    context = {"form": form}
    return render(request, "pybo/comment_form.html", context)


@login_required(login_url="common:login")
def comment_modify_answer(request, comment_id):
    """
    pybo 답글댓글수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, "댓글수정권한이 없습니다")
        return redirect("pybo:detail", question_id=comment.answer.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            # return redirect("pybo:detail", question_id=comment.answer.question.id)

            # pybo:detail에 #comment_2와 같은 앵커를 추가하기 위해 format과 resolve_url 함수를 사용했다.
            # resolve_url 함수는 실제 호출되는 URL을 문자열로 반환하는 장고 함수이다.
            # <a name="comment_{{ comment.id }}"></a> 위치로 스크롤됨
            to = "{}#comment_{}".format(resolve_url("pybo:detail", question_id=comment.answer.question.id), comment.id)
            return redirect(to)
    else:
        form = CommentForm(instance=comment)
    context = {"form": form}
    return render(request, "pybo/comment_form.html", context)


@login_required(login_url="common:login")
def comment_delete_answer(request, comment_id):
    """
    pybo 답글댓글삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, "댓글삭제권한이 없습니다")
        return redirect("pybo:detail", question_id=comment.answer.question.id)
    else:
        comment.delete()
    return redirect("pybo:detail", question_id=comment.answer.question.id)
