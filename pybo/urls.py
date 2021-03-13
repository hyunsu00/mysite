# urls.py
from django.urls import path  # django.urls 패키지에서 path 모듈 가져옴

from .views import base_views, question_views, answer_views, comment_views, vote_views

app_name = "pybo"  # 네임스페이스 정의

urlpatterns = [
    #
    # base_views.py
    #
    # == path('', base_views.IndexView.as_view()),
    path("", base_views.index, name="index"),
    # == path('<int:pk>/', base_views.DetailView.as_view()),
    path("<int:question_id>/", base_views.detail, name="detail"),
    #
    # question_views.py
    #
    # {% url 'pybo:question_create' %}이 추가되었으니 pybo/urls.py 파일에 URL 매핑을 추가
    path("question/create/", question_views.question_create, name="question_create"),
    path("question/modify/<int:question_id>/", question_views.question_modify, name="question_modify"),  # 질문 수정 버튼의 URL 매핑 추가
    path("question/delete/<int:question_id>/", question_views.question_delete, name="question_delete"),  # 질문 삭제 URL 매핑 추가
    #
    # answer_views.py
    #
    path("answer/create/<int:question_id>/", answer_views.answer_create, name="answer_create"),
    path("answer/modify/<int:answer_id>/", answer_views.answer_modify, name="answer_modify"),  # 답변 수정 URL 매핑 추가
    path("answer/delete/<int:answer_id>/", answer_views.answer_delete, name="answer_delete"),  # 답변 삭제 URL 매핑 추가
    #
    # comment_views.py
    #
    # 질문 댓글 URL 매핑 추가
    path("comment/create/question/<int:question_id>/", comment_views.comment_create_question, name="comment_create_question"),  # 댓글 등록
    path("comment/modify/question/<int:comment_id>/", comment_views.comment_modify_question, name="comment_modify_question"),  # 댓글 수정
    path("comment/delete/question/<int:comment_id>/", comment_views.comment_delete_question, name="comment_delete_question"),  # 댓글 삭제
    # 답변 댓글 URL 매핑 추가
    path("comment/create/answer/<int:answer_id>/", comment_views.comment_create_answer, name="comment_create_answer"),  # 댓글 등록
    path("comment/modify/answer/<int:comment_id>/", comment_views.comment_modify_answer, name="comment_modify_answer"),  # 댓글 수정
    path("comment/delete/answer/<int:comment_id>/", comment_views.comment_delete_answer, name="comment_delete_answer"),  # 댓글 삭제
    #
    # vote_views.py
    #
    path("vote/question/<int:question_id>/", vote_views.vote_question, name="vote_question"),  # 질문 추천 URL 매핑
    path("vote/answer/<int:answer_id>/", vote_views.vote_answer, name="vote_answer"),  # 답변 추천 URL 매핑
]
