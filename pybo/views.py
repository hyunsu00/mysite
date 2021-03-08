from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic

from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm

# 페이징 기능 구현
from django.core.paginator import Paginator


def index(request):

    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # order_by 함수는 조회한 데이터를 특정 속성으로 정렬하며, '-create_date'는
    # - 기호가 앞에 붙어 있으므로 작성일시의 역순을 의미한다.
    question_list = Question.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}

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
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

# URL 매핑에 의해 실행될 views.question_create 함수를 작성
# {'form': form}은 템플릿에서 폼 엘리먼트를 생성할 때 사용


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
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()

    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
