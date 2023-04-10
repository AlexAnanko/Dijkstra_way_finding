from django.shortcuts import render, HttpResponse, redirect, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index_page(request):
    """
    Render main page
    :param request: request
    :return: render template 'index.html'
    """
    return render(request, 'index.html')


def signup_page(request):
    """
    This function create and register users

    :param request: POST data from form
    :return: register user

    """

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # Chaeck password matching
        if pass1 != pass2:
            return Http404('403\n\nPasswords does not match ')
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'registration/signup.html')


def login_page(request):
    """
    This function Login users on the site
    :param request: POST data from form
    :return: user

    """
    # Login user on the site
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'registration/login.html')


def logout_page(request):
    """
    Logout user from site
    :param request: request
    :return: main page redirect
    """
    # LogOut user
    logout(request)
    return redirect('index')
