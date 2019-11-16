from django.shortcuts import render
from django.http import HttpResponse
from main.models import Quiz
from django.views.generic import ListView


def quiz_list_view(request):
    quizs_query = Quiz.objects.all()
    return render(request, "list.html", {"quizs": quizs_query})


def main_view(request):
    return render(request, "list.html", {})


def view_about(request):
    return render(request, "main/about.html", {'title': 'About'})


def view_contact(request):
    return render(request, "main/contact.html", {'title': 'Contact'})

