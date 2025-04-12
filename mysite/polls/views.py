from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("polls/index.html")
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse(f"Esta es la pregunta %s." % question_id)

def results(request, question_id):
    response = "Estas viendo los resultados de la pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse(f"Estas votando por la pregunta %s." % question_id)

