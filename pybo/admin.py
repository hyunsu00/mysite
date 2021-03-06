from django.contrib import admin

# 여기에서 모델을 등록하십시오.
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
