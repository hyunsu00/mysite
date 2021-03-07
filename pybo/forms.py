# forms.py

from django import forms
from pybo.models import Question, Answer

# 장고 공식 문서(폼): https://docs.djangoproject.com/en/3.0/topics/forms/
# 장고폼 작성
# 장고 폼은 사실 2개의 폼으로 구분할 수 있는데, forms.Form을 상속받으면 폼, 
# forms.ModelForm을 상속받으면 모델 폼이라 부른다. 
# 모델 폼은 말 그대로 모델과 연결된 폼이며, 모델 폼 객체를 저장하면 연결된 모델의 데이터를 저장할 수 있다.
# 장고 모델 폼은 내부 클래스로 Meta 클래스를 반드시 가져야 하며, 
# Meta 클래스에는 모델 폼이 사용할 모델과 모델의 필드들을 적어야 한다. 
# QuestionForm 클래스는 Question 모델과 연결되어 있으며, 
# 필드로 subject, content를 사용한다고 정의했다.
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        # label 속성 수정하여 Subject, Content 한글로 변경하기
        labels = {
            'subject': '제목',
            'content': '내용',
        }
        # 폼에 부트스트랩 적용하기
        # 수작업으로 폼 작성위해 주석처리
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }