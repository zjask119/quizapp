from django.contrib import admin
from .models import Quiz, Category, Question, Answer


class AnswerInLine(admin.TabularInline):
    model = Answer
    extra = 2
    ordering = ('-answer_text',)


class QuizAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', ]
    list_filter = ['category']
    ordering = ('category', 'name')


class QuestionAdmin(admin.ModelAdmin):
    ordering = ('question_text',)
    inlines = [AnswerInLine]
    list_display = ['quiz', 'question_text', ]
    list_filter = ['quiz']


class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 0


admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
