from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render, redirect
from django.urls import reverse
from dtp.forms import SignUpForm, LoginForm
from dtp.models import User
from dtp.models import Examination


# Render examination list (index) website
def index(request):
    examination_list = Examination.objects.all()
    current_user = request.session['username']
    first_name = request.session['first_name']
    last_name = request.session['last_name']
    return render(request, 'dtp/index.html', {'examination_list': examination_list, 'current_user': current_user,
                                              'first_name': first_name, 'last_name': last_name})


# Render welcome page with login and registration forms.
def welcome(request):
    # Check if request is a POST
    if request.method == 'POST':
        log_form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        # Check if the form sent is login form
        if 'submit_login' in request.POST:
            # Login user if it exists, if it does
            user = authenticate(request, username=username, password=password)
            if user is not None:
                request.session['username'] = username
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                login(request, user)
                return redirect('index')
            else:
                #Display error
                messages.error(request, 'Nazwa użytkownika lub hasło niepoprawne')
                return redirect(reverse('welcome') + '#popup-login')
        # Check if the form sent is registration form
        if 'submit_register' in request.POST:
            reg_form = SignUpForm(request.POST)
            # Check if form is valid
            if reg_form.is_valid():
                # Create and save user with encrypted password
                user = reg_form.save(commit=False)
                user.set_password(password)
                user.save()
                # Login user
                login(request, user)
                return redirect('index')
            else:
                # TODO: Display invalid register
                return redirect(reverse('welcome') + '#popup-regis')
    # Get forms for rendering
    log_form = LoginForm()
    reg_form = SignUpForm()
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
