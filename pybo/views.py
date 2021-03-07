from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic

from .models import Question
from django.utils import timezone

def index(request):
    # order_by 함수는 조회한 데이터를 특정 속성으로 정렬하며, '-create_date'는 
    # - 기호가 앞에 붙어 있으므로 작성일시의 역순을 의미한다.
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}

    # render 함수는 context에 있는 Question 모델 데이터 question_list를 
    # pybo/question_list.html 파일에 적용하여 HTML 코드로 변환한다.
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

# class IndexView(generic.ListView):
#     """
#     pybo 목록 출력
#     """
#     def get_queryset(self):
#         return Question.objects.order_by('-create_date')


# class DetailView(generic.DetailView):
#     """
#     pybo 내용 출력
#     """
#     model = Question

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # ==
    # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    # answer.save()
    return redirect('pybo:detail', question_id=question_id)

