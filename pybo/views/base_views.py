# base_views.py
# 기본 관리

# 페이징 기능 구현
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


def index(request):

    # 입력 파라미터
    page = request.GET.get("page", "1")  # 페이지

    # order_by 함수는 조회한 데이터를 특정 속성으로 정렬하며, '-create_date'는
    # - 기호가 앞에 붙어 있으므로 작성일시의 역순을 의미한다.
    question_list = Question.objects.order_by("-create_date")

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {"question_list": page_obj}

    # render 함수는 context에 있는 Question 모델 데이터 question_list를
    # pybo/question_list.html 파일에 적용하여 HTML 코드로 변환한다.
    return render(request, "pybo/question_list.html", context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "pybo/question_detail.html", context)


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