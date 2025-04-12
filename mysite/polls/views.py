from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola mundo. Estas son las encuestas de la aplicación.")

def detail(request, question_id):
    return HttpResponse(f"Esta es la pregunta %s." % question_id)

def results(request, question_id):
    response = "Estas viendo los resultados de la pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse(f"Estas votando por la pregunta %s." % question_id)

