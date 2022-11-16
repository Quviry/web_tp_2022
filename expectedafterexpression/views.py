from django.shortcuts import render


# Create your views here.

def base(request):
    request.authorised = True
    return render(request, "base.html")


def index(request):
    request.authorised = True
    return render(request, "index.html")


def question(request):
    request.authorised = True
    return render(request, "question.html")


def ask(request):
    request.authorised = True
    return render(request, "ask.html")


def login(request):
    request.authorised = True
    return render(request, "login.html")


def signup(request):
    request.authorised = True
    return render(request, "signup.html")

