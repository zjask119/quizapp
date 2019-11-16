from django.shortcuts import render
from django.http import HttpResponse
from main.models import Quiz
from django.views.generic import ListView


def quiz_list_view(request):
    quizs_query = Quiz.objects.all()
    return render(request, "list.html", {"quizs": quizs_query})


def main_view(request):
    return render(request, "list.html", {})

# Create your views here.
