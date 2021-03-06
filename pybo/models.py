from django.db import models

# 여기에서 모델을 만드세요.


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    # Answer 모델은 어떤 질문에 대한 답변이므로 Question 모델을 속성으로 가져야 한다.
    # 이처럼 어떤 모델이 다른 모델을 속성으로 가지면 ForeignKey를 이용한다.
    # #ForeignKey는 쉽게 말해 다른 모델과의 연결을 의미하며,
    # on_delete=models.CASCADE는 답변에 연결된 질문이 삭제되면 답변도 함께 삭제하라는 의미이다.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
