from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola mundo. Estas son las encuestas de la aplicación.")
