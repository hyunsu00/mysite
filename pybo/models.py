from django.db import models

# 여기에서 모델을 만드세요.
from django.contrib.auth.models import User


class Question(models.Model):

    # Question 데이터에 접근할 경우 author 필드를 기준으로 할지 voter 필드를 기준으로 할지 장고는 알 수 없으므로
    # 'HINT'에 있는 related_name 옵션 추가로 해결
    # 특정 사용자가 작성한 질문을 얻기 위해 some_user.author_question.all() 같은 코드를 사용
    # 특정 사용자가 추천한 질문을 얻기 위한 코드는 some_user.voter_question.all()이다.

    # author 필드는 User 모델을 ForeignKey로 적용하여 선언했다.
    # User 모델은 django.contrib.auth 앱이 제공하는 모델이다.
    # on_delete=models.CASCADE는 계정이 삭제되면 계정과 연결된 Question 모델 데이터를 모두 삭제하라는 의미이다.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_question")

    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    # null=True는 데이터베이스에서 modify_date 칼럼에 null을 허용한다는 의미이며,
    # blank=True는 form.is_valid()를 통한 입력 폼 데이터 검사 시 값이 없어도 된다는 의미이다.
    # 즉, null=True, blank=True는 어떤 조건으로든 값을 비워둘 수 있음을 의미한다.
    modify_date = models.DateTimeField(null=True, blank=True)

    # voter 추가(다대다 관계를 위해 ManyToManyField를 사용)
    voter = models.ManyToManyField(User, related_name="voter_question")

    def __str__(self):
        return self.subject


class Answer(models.Model):
    # Answer 모델은 어떤 질문에 대한 답변이므로 Question 모델을 속성으로 가져야 한다.
    # 이처럼 어떤 모델이 다른 모델을 속성으로 가지면 ForeignKey를 이용한다.
    # #ForeignKey는 쉽게 말해 다른 모델과의 연결을 의미하며,
    # on_delete=models.CASCADE는 답변에 연결된 질문이 삭제되면 답변도 함께 삭제하라는 의미이다.

    # author 필드는 User 모델을 ForeignKey로 적용하여 선언했다.
    # User 모델은 django.contrib.auth 앱이 제공하는 모델이다.
    # on_delete=models.CASCADE는 계정이 삭제되면 계정과 연결된 Question 모델 데이터를 모두 삭제하라는 의미이다.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_answer")

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    # null=True는 데이터베이스에서 modify_date 칼럼에 null을 허용한다는 의미이며,
    # blank=True는 form.is_valid()를 통한 입력 폼 데이터 검사 시 값이 없어도 된다는 의미이다.
    # 즉, null=True, blank=True는 어떤 조건으로든 값을 비워둘 수 있음을 의미한다.
    modify_date = models.DateTimeField(null=True, blank=True)

    # voter 추가(다대다 관계를 위해 ManyToManyField를 사용)
    voter = models.ManyToManyField(User, related_name="voter_answer")


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)