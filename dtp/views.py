from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    return render(request, 'dtp/index.html')


def welcome(request):
    return render(request, 'dtp/welcome.html')


def about(request):
    return render(request, 'dtp/about.html')


def contact(request):
    return render(request, 'dtp/contact.html')


def examination(request, examination_id):
    return HttpResponse("Examination id: %s" % examination_id)


def login_patient(request):
    email = request.POST['email1']
    password = request.POST['pwd1']
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        #TODO: Redirect to examination list page
    #else:
        #TODO: Display invalid login

def login_doctor(request):
    email = request.POST['email1']
    password = request.POST['pwd1']
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        #TODO: Redirect to examination list page
    #else:
        #TODO: Display invalid login


def signup(request):
    if(request.method) == 'POST':
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            email = form.cleaned_data.get('email3')
            password = form.cleaned_data.get('pwd3')
            pow_password = form.cleaned_data.get('pwd4')
            if(pow_password == password):
                user = authenticate(email=email, password=password)
                login(request, user)
                return redirect('/redirect-success/')
            else:
                return None
        else:
            form = UserCreationForm()
    return render(request, 'welcome.html', {'form': form})


def logout(request):
    logout(request)