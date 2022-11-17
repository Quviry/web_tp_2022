from django.shortcuts import render
from django.core.paginator import Paginator


# Pagination logic

def paginate(object_list= [], page_num=1, per_page=10):
    paginator = Paginator(object_list, per_page)
    page_obj = paginator.get_page(page_num)
    return {'page_obj': page_obj}

# Pagination logic end

# mocks


def get_questions():
    return [{
        "title": "title " + str(i),
        "id": i,
        "text": "text" + str(i)
    } for i in range(1, 30)]


# views

def index(request, page=1):
    request.authorised = True
    data = paginate(get_questions(), page, 10)
    return render(request, "index.html", context=data)


def hot(request):
    request.authorised = False
    return render(request, "index.html")


def tag(request):
    request.authorised = False
    return render(request, "index.html")


def question(request, id):
    request.authorised = True
    return render(request, "question.html", context={"id": id})


def ask(request):
    request.authorised = True
    return render(request, "ask.html")


def login(request):
    request.authorised = False
    return render(request, "login.html")


def signup(request):
    request.authorised = False
    return render(request, "signup.html")
