from django.http import HttpResponse

def index(request):
    return HttpResponse("Salam! Polls app-i uğurla işləyir.")

from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    latest_questions = Question.objects.all()
    return render(request, "polls/index.html", {"questions": latest_questions})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
from django.http import HttpResponseRedirect
from django.urls import reverse

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST["choice"])
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse("results", args=(question.id,)))
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
