from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from .models import User
from .forms import LoginForm, CreateUserForm
from donors.forms import DonorDetailsForm
from donors.models import DonorDetails


# def login(request):
#
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(email, password)
#         if len(User.objects.filter(email=email)) == 0:
#             messages.error(request, "User Doesn't Exists")
#         else:
#             user = authenticate(request, email=email, password=password)
#
#             if user is not None:
#                 print(user)
#                 login(user)
#                 return redirect('home')
#             # else:
#             #     messages.error(request, "Password is not matching")
#
#     context = {
#     }
#     return render(request, 'login.html', context)


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
    # if request.method == 'POST':
    #     fname = request.POST.get('fname')
    #     lname = request.POST.get('lname')
    #     email = request.POST.get('email')
    #     pass1 = request.POST.get('pass1')
    #     pass2 = request.POST.get('pass2')
    #     date = request.POST.get('date')
    #     print(date, fname, lname, email, pass1, pass2)
    #
    #     # user = User.objects.create_user(email=email, first_name=fname, last_name=lname,
    #     #                                 password=pass1, date_of_birth=date)
    #     user = authenticate(email=email, password=pass1)
    #     if user is not  None:
    #         login(request, user)
    if request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            dob = form.cleaned_data['date_of_birth']
            password = form.cleaned_data['password']
            print(fname, lname, email, dob, password)
            user = User.objects.create_user(email=email, first_name=fname, last_name=lname,
                                            password=password, date_of_birth=dob)
            # donor = DonorDetails(user=user, blood_group='O+')
            # donor.save()
            return redirect('add_donor_details')

    else:
        form = CreateUserForm()

    context = {
        'form': form
    }

    return render(request, 'signup.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')
