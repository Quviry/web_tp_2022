from django.shortcuts import render
from django.core.paginator import Paginator


# Pagination logic

def paginate(object_list, request, per_page=10):
    page = request.GET.get("page", 1)
    paginator = Paginator(object_list or [], per_page)
    page_obj = paginator.get_page(page)
    page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page, on_each_side=2)
    return {'page_obj': page_obj}

# Pagination logic end

# mocks


def get_questions():
    return [{
        "title": "title " + str(i),
        "id": i,
        "text": "text" + str(i),
        "tags": ["first", "second", "third"]
    } for i in range(1, 1000)]


# views

def index(request, page=1):
    request.authorised = True
    data = paginate(get_questions(), request, 10)
    return render(request, "index.html", context=data)


def hot(request, page=1):
    request.authorised = True
    data = paginate(get_questions(), request, 10)
    return render(request, "hot.html", context=data)


def tag(request, tag_name="tag", page=1):
    request.authorised = True
    data = paginate(get_questions()[::2], request, 10)
    data["tag"] = tag_name
    return render(request, "tag.html", context=data)


def question(request, id=1):
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
