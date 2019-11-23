from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseNotFound, Http404
from main.models import Quiz, Category
from django.views.generic import ListView
from django.http import Http404





def quiz_list_view(request):
    return render(request, "main/list.html", {})


def view_about(request):
    return render(request, "main/about.html", {'title': 'About'})


def view_contact(request):
    return render(request, "main/contact.html", {'title': 'Contact'})


def category_view(request):
    quizs_query = Quiz.objects.all()
    categorys_query = Category.objects.all()
    return render(request, "main/list.html", {"categorys": categorys_query, "quizs": quizs_query })





