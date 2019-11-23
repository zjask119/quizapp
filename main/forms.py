from django import forms
from .models import Quiz, Question, Answer


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = [
            'name',
            'category',
            'description'
        ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'question_text'
        ]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'answer_text',
            'is_correct'
        ]


AnswerFormSet = forms.modelformset_factory(
    Answer,
    form=AnswerForm
)
