from django.shortcuts import render
from main.models import Quiz, Category, Question, Answer
from django.http import Http404


def quiz_list_view(request):
    return render(request, "main/list.html", {})


def quiz_detail(request, quiz_pk):
    try:
        quiz = Quiz.object.get(pk=quiz_pk)
    except Quiz.DoesNotExist:
        raise Http404("Quiz does not exist!")

    questions = Question.objects.filter(quiz=quiz)
    answers = Answer.objects.filter(question__quiz=quiz)

    context = {"quiz": quiz,
               "questions": questions,
               "answers": answers
               }
    return render(request, "main/quiz_detail.html", context)


def view_about(request):
    return render(request, "main/about.html", {'title': 'About'})


def view_contact(request):
    return render(request, "main/contact.html", {'title': 'Contact'})


def category_view(request):
    quizs_query = Quiz.objects.all()
    categorys_query = Category.objects.all()
    return render(request, "main/list.html", {"categorys": categorys_query, "quizs": quizs_query})
