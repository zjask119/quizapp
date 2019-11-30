from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Quiz, Category, Answer, Question
from main.forms import QuizForm, QuestionForm, AnswerForm


def view_about(request):
    return render(request, "main/about.html", {'title': 'About'})


def view_contact(request):
    return render(request, "main/contact.html", {'title': 'Contact'})


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
            return redirect(f'question_create/{form.instance.id}/')
        else:
            raise Http404("Quiz does not exist!")
    else:
        form = QuizForm()
        return render(request, 'main/quiz_form.html', {'form': form})


@login_required
def question_create(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.instance.quiz = quiz
            form.save()
            messages.success(request, f'Question has been added. Now add answers!')
            return redirect('answer_create', quiz_id=quiz_id, question_id=form.instance.id)
        else:
            raise Http404("Question does not exist!")
    else:
        form = QuestionForm()
        return render(request, 'main/question_form.html', {'form': form, 'name': 'Add question'})


@login_required
def answer_create(request, quiz_id, question_id):
    question = Question.objects.get(pk=question_id)

    if request.method == 'POST':
        data = request.POST
        if data.get('new_question'):
            return redirect('question_create', quiz_id=quiz_id)
        if data.get('exit'):
            return redirect('home')
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.instance.question = question
            form.save()
            messages.success(request, f'Answer has been added')
            return redirect('answer_create', quiz_id=quiz_id, question_id=question_id)
        else:
            raise Http404("Question does not exist!")
    else:
        form = AnswerForm()
        return render(request, 'main/question_form.html', {'form': form, 'name': 'Add answer'})


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


def view_by_category(request):
    quizes = Quiz.objects.all()
    category_pk = request.GET.get('filter')
    category = Category.objects.get(pk=category_pk)
    if category:
        quizes = Quiz.objects.filter(category__pk=category_pk)
    return render(request, 'main/category_list.html', {'quizes': quizes, 'category': category})
