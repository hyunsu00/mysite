# urls.py
from django.urls import path  # django.urls 패키지에서 path 모듈 가져옴

from . import views  # 현재 패키지에서 views 모듈 가져옴

app_name = 'pybo'  # 네임스페이스 정의

urlpatterns = [
     # == path('', views.IndexView.as_view()),
     path('', views.index, name='index'),
     # == path('<int:pk>/', views.DetailView.as_view()),
     path('<int:question_id>/', views.detail, name='detail'),
     path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
     # {% url 'pybo:question_create' %}이 추가되었으니 pybo/urls.py 파일에 URL 매핑을 추가
     path('question/create/', views.question_create, name='question_create'),
     path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),  # 질문 수정 버튼의 URL 매핑 추가
     path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),  # 질문 삭제 URL 매핑 추가
     path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),  # 답변 수정 URL 매핑 추가
     path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),  # 답변 삭제 URL 매핑 추가
     # 질문 댓글 URL 매핑 추가
     path('comment/create/question/<int:question_id>/', views.comment_create_question, name='comment_create_question'),  # 댓글 등록
     path('comment/modify/question/<int:comment_id>/', views.comment_modify_question, name='comment_modify_question'),  # 댓글 수정
     path('comment/delete/question/<int:comment_id>/', views.comment_delete_question, name='comment_delete_question'),  # 댓글 삭제
     # 답변 댓글 URL 매핑 추가
     path('comment/create/answer/<int:answer_id>/', views.comment_create_answer, name='comment_create_answer'), # 댓글 등록
     path('comment/modify/answer/<int:comment_id>/', views.comment_modify_answer, name='comment_modify_answer'), # 댓글 수정
     path('comment/delete/answer/<int:comment_id>/', views.comment_delete_answer, name='comment_delete_answer'), # 댓글 삭제
]
