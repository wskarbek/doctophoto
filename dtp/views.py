from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render, redirect
from dtp.forms import SignUpForm, LoginForm
from dtp.models import User
from dtp.models import Examination


# Views
def index(request):
    examination_list = Examination.objects.all()
    return render(request, 'dtp/index.html', {'examination_list': examination_list})


def welcome(request):
    log_form = LoginForm()
    reg_form = SignUpForm()
    # Check if request is a POST
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if 'submit_login' in request.POST:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                # TODO: Display invalid login
                return redirect('welcome')
        if 'submit_register' in request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(password)
                user.save()
                login(request, user)
                return redirect('index')
            else:
                # TODO: Display invalid register
                return redirect('welcome')

    # Render welcome page
    return render(request, 'dtp/welcome.html', {'reg_form': reg_form, 'log_form': log_form})


def about(request):
    return render(request, 'dtp/about.html')


def contact(request):
    return render(request, 'dtp/contact.html')


def examination(request, exam_id):
    exam = Examination.objects.get(id=exam_id)
    return render(request, 'dtp/examination.html', {'exam': exam})


# Controllers
def logout(request):
    logout(request)
