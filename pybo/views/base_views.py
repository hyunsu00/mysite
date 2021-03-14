# base_views.py
# 기본 관리

# 페이징 기능 구현
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from django.db.models import Q, Count

from ..models import Question


def index(request):

    """
    pybo 목록출력
    """

    # 입력 파라미터
    page = request.GET.get("page", "1")  # 페이지
    kw = request.GET.get("kw", "")  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    # order_by 함수는 조회한 데이터를 특정 속성으로 정렬하며, '-create_date'는
    # - 기호가 앞에 붙어 있으므로 작성일시의 역순을 의미한다.
    # 정렬
    if so == 'recommend':
        # 추천 수가 큰 것부터 정렬하므로 order_by에 추천 수 -num_voter를 입력
        # Question.objects.annotate(num_voter=Count('voter'))에서 사용한 annotate 함수는 
        # Question 모델의 기존 필드인 author, subject, content, create_date, modify_date, voter에 
        # 질문의 추천 수에 해당하는 num_voter 필드를 임시로 추가해 주는 함수이다.
        # 이렇게 annotate 함수로 num_voter 필드를 추가하면 filter 함수나 order_by 함수에서 
        # num_voter 필드를 사용할 수 있게 된다. 여기서 num_voter는 Count('voter')와 같이 
        # Count 함수를 사용하여 만들었다. Count('voter')는 해당 질문의 추천 수이다.
        # order_by('-num_voter', '-create_date')와 같이 order_by 함수에 두 개 이상의 인자가 전달되는 경우 
        # 1번째 항목부터 우선순위를 매긴다. 즉, 추천 수가 같으면 최신순으로 정렬한다.
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')

    # Q 함수에 사용된 subject__icontains=kw는 제목에 kw 문자열이 포함되었는지를 의미한다.
    # answer__author__username__icontains은 답변을 작성한 사람의 이름에 포함되는지를 의미한다.
    # filter 함수에서 모델 필드에 접근하려면 이처럼 __를 이용하면 된다.
    # subject__contains=kw 대신 subject__icontains=kw을 사용하면 대소문자를 가리지 않고 찾아 준다.
    # 1개의 질문에는 여러 개의 답변이 있을수 있으므로 답변자 중복을 처리하기 위해 distinct 함수를 반드시 사용해야 한다.
    if kw:
        # 제목검색 or 내용검색 or 질문 글쓴이검색 or 답변 글쓴이검색
        question_list = question_list.filter(
            Q(subject__icontains=kw) | 
            Q(content__icontains=kw) | 
            Q(author__username__icontains=kw) | 
            Q(answer__author__username__icontains=kw)
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {"question_list": page_obj, "page": page, "kw": kw, 'so': so}  # page와 kw, so가 추가되었다.

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