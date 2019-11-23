from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseNotFound, Http404
from main.models import Quiz, Question, Answer
from django.views.generic import ListView
from django.http import Http404


def quiz_list_view(request):
    quizs_query = Quiz.objects.all()
    return render(request, "main/list.html", {"quizs": quizs_query})


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
