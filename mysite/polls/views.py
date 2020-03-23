from django.http import HttpResponse


def index(request):
    return HttpResponse("Goodbye, world. You're at the polls index.")
