from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def collection(request):
    return render(request, "collection.html")


def contact(request):
    return render(request, "contact.html")


def projects(request):
    return render(request, "projects.html")