from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from main.models import Quiz, Category, Answer
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage
from .forms import QuizForm


def view_about(request):
    return render(request, "main/about.html", {'title': 'About'})


def view_contact(request):
    return render(request, "main/contact.html", {'title': 'Contact'})


def quiz_list_view(request):
    return render(request, "main/list.html", {})


def quiz_detail(request, quiz_pk):
    try:
        quiz = Quiz.objects.get(pk=quiz_pk)
    except Quiz.DoesNotExist:
        raise Http404("Quiz does not exist!")

    quiz_data = []
    for question in quiz.question.all():
        quiz_data.append({'questions': question.question_text, 'id': question.pk,
                          'answers': [{'id': answer.pk, 'text': answer.answer_text} for answer in
                                      question.answer.all()]})

    context = {"quiz_data": quiz_data, "quiz": quiz}
    return render(request, "main/quiz_detail.html", context)


def quiz_check(request):
    score = 0
    max_score = 0

    answers = [
        value
        for key, value in request.POST.items()
        if key.startswith('value-')
    ]

    for answer in answers:
        ans = Answer.objects.get(pk=answer)
        max_score += 1
        if ans.is_correct:
            score += 1

    result = float(score / max_score) * 100
    context = {'score': score, 'max_score': max_score, 'result': result}
    return render(request, "main/score.html", context)


@login_required
def quiz_create(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, f'Quiz has been added!')
            return redirect('/')
    else:
        form = QuizForm()
    return render(request, 'main/quiz_form.html', {'form': form})


def category_view(request):
    quiz_page = request.GET.get('page_quiz', 1)
    quizs_query = Quiz.objects.all()
    paginator = Paginator(quizs_query, 3)
    categorys_query = Category.objects.all()
    try:
        quizs = paginator.page(quiz_page)
    except EmptyPage:
        quizs = paginator.page(paginator.num_pages)
    return render(request, "main/list.html", {"categorys": categorys_query, "quizs": quizs})
