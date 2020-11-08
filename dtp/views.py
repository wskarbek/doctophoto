from django.shortcuts import HttpResponse, render


# Create your views here.

def index(request):
    return render(request, 'dtp/index.html')


def welcome(request):
    return render(request, 'dtp/welcome.html')


def examination(request, examination_id):
    return HttpResponse("Examination id: %s" % examination_id)