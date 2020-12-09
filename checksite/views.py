from django import HttpResponse


def index(request):
    return HttpResponse("<h4>Hello</h4>")