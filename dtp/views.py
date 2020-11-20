from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render, redirect
from dtp.forms import SignUpForm, LoginForm
# Create your views here.


def index(request):
    return render(request, 'dtp/index.html')


def welcome(request):
    form3 = SignUpForm()
    return render(request, 'dtp/welcome.html', {'form3': form3})


def about(request):
    return render(request, 'dtp/about.html')


def contact(request):
    return render(request, 'dtp/contact.html')


def examination(request):
    return render(request, 'dtp/examination.html')


def login_patient(request):
    if(request.method == 'POST'):
        form = LoginForm(request.POST)
        email = request.POST['email1']
        password = request.POST['pwd1']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/account/login/patient')
        else:
            #TODO: Display invalid login
            return redirect('views.welcome')

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
    form_class = SignUpForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            #pow_password = form.pow_password
            form.save()
            user = authenticate(email=email, password=password)
            login(request, user)
            return HttpResponseRedirect('welcome')
        else:
            return HttpResponseRedirect('welcome')
    else:
        form = form_class()
    return render(request, 'welcome', {'form': form })

#pog2
def logout(request):
    logout(request)