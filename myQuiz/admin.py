# Register your models here.
from django.contrib import admin

from .models import Question
from myQuiz.models import Choice

admin.site.register(Question)
admin.site.register(Choice)
