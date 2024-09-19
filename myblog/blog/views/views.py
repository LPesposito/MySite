from django.http import HttpResponse


def home(request):
    return HttpResponse("HELLO WORLD!!!")


def Posts(request):
    return HttpResponse("Hello World!")
