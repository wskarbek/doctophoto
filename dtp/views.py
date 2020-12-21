from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render, redirect
from dtp.forms import SignUpForm, LoginPatientForm
from dtp.models import User

# Create your views here.
from dtp.models import Examination
def clean_login(self):
    data = self.cleaned_data['username']
    none_users = User.objects.filter(username=data)
    if none_users.exists() == False:
        return redirect('welcome')
    return data

def index(request):
    examination_list = Examination.objects.all()
    return render(request, 'dtp/index.html', {'examination_list': examination_list})


def welcome(request):
    log_patient_form = LoginPatientForm()
    reg_form = SignUpForm()
    return render(request, 'dtp/welcome.html', {'reg_form': reg_form, 'log_patient_form': log_patient_form})


def about(request):
    return render(request, 'dtp/about.html')


def contact(request):
    return render(request, 'dtp/contact.html')


def examination(request, exam_id):
    exam = Examination.objects.get(id=exam_id)
    return render(request, 'dtp/examination.html', {'exam': exam})


def login_patient(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)
            if user.check_password(password) is True:
                login(request, user)
                return redirect('index')
            else:
                #TODO: Display invalid login
                return redirect('welcome')
        except User.DoesNotExist:
            return redirect('welcome')

def login_doctor(request):
    #TODO: this function needs to check if the user is a doctor
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username)
        if user.check_password(password) is True:
            login(request, user)
            print("Logged in as", user)
            return redirect('index')
        else:
            #TODO: Display invalid login
            print("invalid login")
            return redirect('welcome')


def signup(request):
    form_class = SignUpForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('index')
        else:
            return redirect('welcome')
    else:
        form = form_class()


def logout(request):
    logout(request)
