from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Django Site with no Applications!</h1>")
