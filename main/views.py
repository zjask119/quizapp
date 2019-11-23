from django.shortcuts import render
from main.models import Quiz, Category, Question, Answer
from django.http import Http404


def quiz_list_view(request):
    return render(request, "main/list.html", {})


def quiz_detail(request, quiz_pk):
    try:
        quiz = Quiz.objects.get(pk=quiz_pk)
    except Quiz.DoesNotExist:
        raise Http404("Quiz does not exist!")

    quiz_data = []
    for question in Quiz.question.all():
        quiz_data.append({'questions': question.question_text,
                          'answers': [answer.answer_text for answer in question.answer.all()]})

    context = {"quiz_data": quiz_data}
    return render(request, "main/quiz_detail.html", context)


def view_about(request):
    return render(request, "main/about.html", {'title': 'About'})


def view_contact(request):
    return render(request, "main/contact.html", {'title': 'Contact'})


def category_view(request):
    quizs_query = Quiz.objects.all()
    categorys_query = Category.objects.all()
    return render(request, "main/list.html", {"categorys": categorys_query, "quizs": quizs_query})
