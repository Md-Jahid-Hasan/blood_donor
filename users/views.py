from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from .models import User
from .forms import LoginForm, CreateUserForm
from donors.forms import DonorDetailsForm
from donors.models import DonorDetails
import random
from blood_doner.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


def user_login(request):
    if request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            # print("User: ", user)
            if user:
                login(request, user)
            return redirect("/")
    else:
        form = LoginForm()

    context = {
        'form': form
    }

    return render(request, 'login.html', context)


def create_user(request):
    if request.method == 'POST':
        print("Hello json")

    if request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            dob = form.cleaned_data['date_of_birth']
            password = form.cleaned_data['password']
            bg = form.cleaned_data['blood_group']

            key = random.randint(1000, 9999)
            request.session['token'] = key
            print(key)
            subject = 'Welcome!'
            message = 'Welcome to My site.'
            recepient = str(email)

            mail_counter = send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=True)
            print(mail_counter, "Print mail counter")

            user = User.objects.create_user(email=email, first_name=fname, last_name=lname,
                                            password=password, date_of_birth=dob)
            request.session['user'] = email
            donor = DonorDetails(user=user, blood_group=bg)
            donor.save()
            return redirect('login')

    else:
        form = CreateUserForm()

    context = {
        'form': form
    }

    return render(request, 'signup.html', context)


def user_logout(request):
    logout(request)
    return redirect(request.GET.get('next'))


def validate_user(request):
    try:
        key = request.session['token']
        user = request.session['user']
    except:
        return redirect('login')

    print(user, key)
    if request.method == "POST":
        k = int(request.POST.get('key'))
        if k == key:
            del request.session['token']
            del request.session['user']
            print("Delete")


    context = {

    }
    return render(request, 'validate.html', context)
